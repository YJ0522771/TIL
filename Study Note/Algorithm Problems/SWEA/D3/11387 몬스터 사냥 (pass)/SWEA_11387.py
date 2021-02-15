import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    print('#{}'.format(test_case), end=' ')

    D, L, N = map(int, input().split())
    print(D, L, N)
    result = D * 0.01 * L * N * (N - 1) // 2
    result += N * D

    print(int(result))

