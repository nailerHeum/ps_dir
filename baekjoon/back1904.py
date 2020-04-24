from sys import stdin
N = int(stdin.readline())
arr = [0] * 1000001
arr[0], arr[1] = 1, 2
for i in range(2, N):
    arr[i] = (arr[i-2] + arr[i-1]) % 15746

print(arr[N-1])