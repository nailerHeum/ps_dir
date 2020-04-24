from sys import stdin
T = int(stdin.readline())
tests = []
for t in range(T):
    tests.append(int(stdin.readline()))
for i in range(len(tests)):
    count = 1
    case = tests[i]
    while case > 1:
        last_digit = str(case)[-1]
        if last_digit != '1':
            if last_digit == '0':
                ticks = 9
            else:
                ticks = int(last_digit) - 1
            count += ticks
            case -= ticks
        rev = int(str(case)[::-1])
        if rev < case and len(str(rev)) == len(str(case)):
            case = rev
            count += 1
        else:
            case -= 10
            count += 10
    print(f'Case #{i + 1}: {count}')