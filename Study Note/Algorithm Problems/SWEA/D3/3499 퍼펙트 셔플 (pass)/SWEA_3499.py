import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    word = list(input().split())
    is_odd = N % 2
    t = (N // 2) + is_odd
    half1 = word[:t]
    half2 = word[t:N]
    res = ''
    for i in range(t - is_odd):
        res += half1[i] + ' ' + half2[i] + ' '
    if is_odd:
        res += half1[t - 1]

    print('#{} {}'.format(test_case, res))