from sys import stdin
from collections import Counter
N = int(stdin.readline())
plist = []
for i in range(0, N):
  plist.append(stdin.readline()[0])
answer = []
c = Counter(plist)
for k in c.keys():
  if c[k] < 5:
    continue
  answer.append(k)
if not answer:
  print('PREDAJA')
else:
  print(''.join(sorted(answer)))