import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N, K = map(int, input().split())
    count = [0] * N
    submit = list(map(int, input().split()))
    for s in submit:
        count[s-1] += 1
    print('#{}'.format(test_case), end='')
    for i in range(N):
        if not count[i]:
            print(' {}'.format(i + 1), end='')
    print()

