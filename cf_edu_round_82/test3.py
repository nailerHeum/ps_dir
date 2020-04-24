from sys import stdin
from string import ascii_lowercase

T = int(stdin.readline())
tests = []
for t in range(T):
    tests.append(stdin.readline())

for test in tests:
    remainedChars = list(ascii_lowercase)
    remainedChars.remove(test[0])
    keysetting = [test[0]]
    head = 0
    impossible = False
    test = test[:-1]
    for i in range(1, len(test)):
        if head == 0:
            if head == len(keysetting) - 1:
                keysetting.append(test[i])
                remainedChars.remove(test[i])
                head += 1
            else:
                if keysetting[head + 1] == test[i]:
                    head += 1
                else:
                    keysetting.insert(0, test[i])
                    try:
                        remainedChars.remove(test[i])
                    except:
                        impossible = True
                        break
            continue
        if head == len(keysetting) - 1:
            if keysetting[head - 1] == test[i]:
                head -= 1
            else:
                keysetting.append(test[i])
                head += 1
                try:
                    remainedChars.remove(test[i])
                except:
                    impossible = True
                    break
        else:
            if keysetting[head + 1] == test[i]:
                head += 1
            elif keysetting[head - 1] == test[i]:
                head -= 1
            else:
                impossible = True
                break
    if impossible:
        print('NO')
        continue
    print('YES')
    print(f"{''.join(keysetting) + ''.join(remainedChars)}")