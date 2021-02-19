import sys
sys.stdin = open("input.txt", "r")

arr = [1, 1, 1, 2, 2]
n = 5
while n < 100:
    arr.append(arr[n - 1] + arr[n - 5])
    n += 1

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    print('#{} {}'.format(test_case, arr[N - 1]))