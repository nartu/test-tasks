import os
from collections import Counter
# <host>\t<ip>\t<page>\n

base_dir = os.path.dirname(os.path.abspath(__file__))
dataset = os.path.join(base_dir,'datasets','hits.txt')

ips_raw = list()
# c = 1
with open(dataset) as file:
    # <host>\t<ip>\t<page>\n
    for line in file:
        ips_raw += [line.split('\t')[1]]
        # c += 1
        # if c >=100: break

ips = Counter()
for ip in ips_raw:
    ips[ip] += 1
ips_popular = ips.most_common(5)
[print('{}\t{}'.format(ipp[0],ipp[1])) for ipp in ips_popular]
# print(len(ips))
# print(len(ips_raw))











# import collections
# c = collections.Counter()
# # d = dict()
# ar = ['spam', 'egg', 'spam', 'counter', 'counter', 'counter']
# for word in ar:
#     c[word] += 1
# d = dict.fromkeys(ar,1)
# print(c.most_common(2))
#
# print(c)
# print(d)
