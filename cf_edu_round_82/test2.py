from sys import stdin
from math import ceil
T = int(stdin.readline())
tests = []
for t in range(T):
    n, g, b = [int(x) for x in stdin.readline().split(' ')]
    tests.append((n, g, b))
for test in tests:
    n, g, b = test
    count = 0
    availbad = n // 2
    coolticks = ceil(availbad / b)
    if n <= coolticks * g + availbad:
        print(n)
        continue
    count += coolticks * (g + b)
    n -= coolticks * g + availbad
    moretick, remain = divmod(n, g)
    count += moretick * (g + b) + remain
    if moretick >= 1 and remain == 0:
        print(count - b)
    else:
        print(count)