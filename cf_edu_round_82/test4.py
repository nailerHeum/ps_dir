from sys import stdin
T = int(stdin.readline())

for t in range(T): 
    n, m = [int(x) for x in stdin.readline().split(' ')]
    mlist = [int(x) for x in stdin.readline().split(' ')]
    if sum(mlist) < n:
        print('-1')
        continue
    nb = format(n, 'b')
    nm = format(sum(mlist), 'b')
    nb = nb[::-1]
    nm = nm[::-1]
    count, counter = 0, False
    for i in range(len(nm)):
        if len(nb) == i:
            break
        if nb[i] == 0:
            if counter and nm[i] != '1':
                count += 1
            else:
                continue
            
for test in tests:
    
# 가방이 n짜리 사이즈
# m 개의 box
# i 번째 박스의 사이즈는 a(i)
# integer non negative power of two (2의 제곱쑤)
# box들을 똑같은 사이즈의 두개로 나눌 수 있다. bag을 채우는 게 목표
# n 존나 큼, m <= 100000