from sys import stdin

T = int(stdin.readline())

def bfs(idx, checker, rdict):
    counter = 0
    for val in rdict[idx]:
        if checker[val]:
            continue
        counter += 1
        checker[val] = True
        counter += bfs(val, checker, rdict)
    return counter

for t in range(T):
    reldict = {}
    N, M = map(int, stdin.readline().split(' '))
    for m in range(M):
        a, b = map(int, stdin.readline().split(' '))
        try:
            reldict[a].append(b)
        except:
            reldict[a] = [b]
        try:
            reldict[b].append(a)
        except:
            reldict[b] = [a]
    all_lands = reldict.keys()
    checklist = dict(zip(all_lands, [False] * len(reldict)))
    head = list(all_lands)[0]
    count = 0
    checklist[head] = True
    print(bfs(head, checklist, reldict))
        