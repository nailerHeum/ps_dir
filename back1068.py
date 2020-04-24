from sys import stdin

N = int(stdin.readline())
nodes = [int(x) for x in stdin.readline().split(' ')]
delnode = int(stdin.readline())
parent_count = 0

dellist = [delnode]

if delnode in nodes:
  parent_count -= 1

for i in range(N):
  if nodes[i] in dellist:
    dellist.append(i)
    continue
  if i in nodes:
    parent_count += 1

print(len(nodes) - len(dellist) - parent_count)