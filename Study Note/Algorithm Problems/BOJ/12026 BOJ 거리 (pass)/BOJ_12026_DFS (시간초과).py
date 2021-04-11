import sys
sys.stdin = open("input.txt", "r")


def solve(cur, i, s):
    global res
    if i == N - 1:
        if res > s:
            res = s
        return
    c = 'BOJ'[('BOJ'.index(cur) + 1) % 3]

    for j in range(i + 1, N):
        if road[j] == c:
            solve(c, j, s + (j - i)**2)
    return


N = int(input())
road = list(input())

res = 1000001
solve('B', 0, 0)

if res == 1000001:
    print(-1)
else:
    print(res)
