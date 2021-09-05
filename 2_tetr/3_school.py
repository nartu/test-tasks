import os

base_dir = os.path.dirname(os.path.abspath(__file__))
l_lessons = os.path.join(base_dir,'datasets','tech_quality','lessons.txt')
l_users = os.path.join(base_dir,'datasets','tech_quality','users.txt')
l_participants = os.path.join(base_dir,'datasets','tech_quality','participants.txt')
l_quality = os.path.join(base_dir,'datasets','tech_quality','quality.txt')

# fetch users [list] user_id
# ['id', 'role'] tutor only
cu = 0
users = list()
with open(l_users) as file:
    for line in file:
        if cu>1 and '|' not in line:
            break         # end of file
        if cu>1:
            tmp = list(map(lambda t: t.strip(),line.split('|')))
            if tmp[1] == 'tutor':
                users += [tmp[0]]
        cu += 1

# fetch participants [dict] event_id -> user_id
# ['event_id', 'user_id'] tutor only
cp = 0
participants = dict()
with open(l_participants) as file:
    for line in file:
        if cp>1 and '|' not in line:
            break         # end of file
        if cp>1:
            tmp = list(map(lambda t: t.strip(),line.split('|')))
            if tmp[1] in users:
                participants[tmp[0]] = tmp[1]
        cp += 1

# fetch quality [dict] lesson_id -> tech_quality
# ['lesson_id', 'tech_quality']
cq = 0
quality = dict()
with open(l_quality) as file:
    for line in file:
        if cq>1 and '|' not in line:
            break         # end of file
        if cq>1:
            tmp = list(map(lambda t: t.strip(),line.split('|')))
            if tmp[0] not in quality:
                quality[tmp[0]] = []
            if tmp[1].isdigit():
                q = [int(tmp[1])]
            else:
                q = []
            quality[tmp[0]] += q
        cq += 1

# fetch lesson
# ['id', 'event_id', 'subject', 'scheduled_time']
cl = 0
lesson = dict()
with open(l_lessons) as file:
    for line in file:
        if cl>1 and '|' not in line:
            break         # end of file
        if cl>1:
            tmp = list(map(lambda t: t.strip(),line.split('|')))
            # print(tmp)
            if tmp[2] == 'phys':
                # date gouping
                date = tmp[3][:10]
                if date not in lesson.keys():
                    lesson[date] = {}
                # tutor grouping
                tutor = participants[tmp[1]]
                if tutor not in lesson[date]:
                    lesson[date][tutor] = []
                # quality list for tutors
                if tmp[0] in quality:
                    tmp_quality = quality[tmp[0]]
                else:
                    tmp_quality = []
                lesson[date][tutor] += tmp_quality
        cl += 1
#         if cl>=50:
#             cl = 0
#             break

# out
# <день> <id учителя> <средняя арифметическая оценка>
out = []
c = 0
for date,body in lesson.items():
    out += [{
        'date': date,
        'tutor_min': '',
        'quality_min': 6,
    }]
    for tutor,q in body.items():
        if len(q)>0:
            av_q = round(sum(q)/len(q),2)
        if av_q < out[c]['quality_min']:
            out[c]['quality_min'] = av_q
            out[c]['tutor_min'] = tutor
    c += 1
for line in sorted(out,key=lambda k: k['date']):
    print(*line.values())
