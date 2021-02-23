import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    mem = list(map(int, list(input())))
    N = len(mem)
    current = 0
    count = 0
    for i in range(N):
        if mem[i] != current:
            current = not current
            count += 1

    print('#{} {}'.format(test_case, count))