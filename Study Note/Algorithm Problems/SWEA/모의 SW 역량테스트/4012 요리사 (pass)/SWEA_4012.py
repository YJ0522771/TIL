import sys
sys.stdin = open("input.txt", "r")


def solve(k):
    global res
    global A
    global B
    global memo
    if len(A) > N // 2 or len(B) > N // 2:
        return
    if k >= N:
        a = ''.join(map(str, A))
        b = ''.join(map(str, B))
        if a in memo:
            return
        memo.append(a)
        memo.append(b)
        temp = 0
        for a in A:
            for j in A:
                temp += S[a][j]
        for b in B:
            for j in B:
                temp -= S[b][j]
        temp = abs(temp)
        if res > temp:
            res = temp
        return

    A.append(k)
    solve(k + 1)
    A.pop()
    B.append(k)
    solve(k + 1)
    B.pop()
    return

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    A = []
    B = []
    memo = []
    res = 1000000
    solve(0)
    print('#{} {}'.format(test_case, res))
