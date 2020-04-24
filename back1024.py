from sys import stdin
N, L = map(int, stdin.readline().split(' '))
hasAnswer = False
for amount in range(L, 101):
  div, mod = divmod(N, amount)
  if mod == 0 and amount % 2 == 1:
    initialValue = div - amount // 2
    if initialValue < 0:
      break
    print(' '.join([str(x) for x in range(initialValue, initialValue + amount)]))
    hasAnswer = True
    break
  if float(mod) == amount / 2 and amount % 2 == 0:
    initialValue = div - (amount // 2 - 1)
    if initialValue < 0:
      break
    print(' '.join([str(x) for x in range(initialValue, initialValue + amount)]))
    hasAnswer = True
    break
if not hasAnswer:
  print('-1')