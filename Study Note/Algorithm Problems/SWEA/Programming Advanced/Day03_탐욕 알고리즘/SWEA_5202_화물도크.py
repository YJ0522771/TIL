import sys
sys.stdin = open("input.txt", "r")
# 활동선택 (Activity-selection) 문제

T = int(input())
for test_case in range(1, T + 1):
    # ////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////////////////////
    N = int(input())
    TT = [tuple(map(int, input().split())) for _ in range(N)]

    # 끝나는 시간 순으로 정렬한 다음 시간이 겹치지 않는 것들만 나열한다.
    TT.sort(key=lambda x : (x[1]))
    # print(TT)
    res = 0
    start = 0
    for t in TT:
        if t[0] >= start:
            start = t[1]
            res += 1
    print('#{} {}'.format(test_case, res))