import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////
    r = list(map(int, input().split()))
    for i in r:
        if r.count(i) % 2:
            print('#{} {}'.format(test_case, i))
            break