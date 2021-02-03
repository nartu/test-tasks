import os

base_dir = os.path.dirname(os.path.abspath(__file__))
dataset = os.path.join(base_dir,'datasets','names.txt')

def alpha_count(word):
    a = ord('A')
    z = ord('Z') + 1
    # alpha = dict()
    # for i in range(a,z):
    #     alpha[chr(i)] = i-a+1
    # return alpha
    sum = 0
    for i in word:
        sum += ord(i)-a+1
    return sum

with open(dataset) as file:
    ar = file.read().split(',')
names = sorted(list(map(lambda t: t[1:len(t)-1], ar)))
print(alpha_count('MAY'))
print(names.index('MAY'))

ans  = dict()
index = 1
sum_all = 0
for name in names:
    # ans[name] = {'count': index, 'sum': alpha_count(name)}
    # if index >= 7: break
    sum_all += index * alpha_count(name)
    index += 1

print(sum_all)
