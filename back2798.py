from sys import stdin
from itertools import combinations

N, M = [int(x) for x in stdin.readline().split(' ')]
numlist = [int(x) for x in stdin.readline().split(' ') if int(x) < M]

candis = combinations(numlist, 3)

answer = max(filter(lambda x: x <= M, map(sum, candis)))
print(answer)