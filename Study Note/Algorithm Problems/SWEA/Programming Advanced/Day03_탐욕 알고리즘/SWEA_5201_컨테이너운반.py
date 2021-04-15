import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    TT = list(map(int, input().split()))

    W.sort()
    TT.sort()
    res = 0
    while len(TT) and len(W):
        t = TT.pop()
        while len(W):
            w = W.pop()
            # 현재 대기 중인 트럭의 용량이 뽑은 짐의 무게보다 작으면 다시 뽑는다.
            if t >= w:
                res += w
                break
    print('#{} {}'.format(test_case, res))
