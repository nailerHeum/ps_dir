from sys import stdin
N = int(stdin.readline())
tests = []
for i in range(N):
    tests.append(stdin.readline())
for test in tests:
    start = test.find('1')
    end = test.rfind('1') + 1
    count = 0
    for ch in list(test[start:end]):
        if ch == '0':
            count += 1
    print(count)