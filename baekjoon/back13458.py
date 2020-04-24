from sys import stdin
answer = 0
N = int(stdin.readline())
classrooms = [int(x) for x in stdin.readline().split(' ')]
B, C = [int(x) for x in stdin.readline().split(' ')]

answer += N
classrooms = filter(lambda x: x > 0, map(lambda x: x - B, classrooms))

for room in classrooms:
  div, mod = divmod(room, C)
  answer += div
  if mod > 0:
    answer += 1
print(answer)