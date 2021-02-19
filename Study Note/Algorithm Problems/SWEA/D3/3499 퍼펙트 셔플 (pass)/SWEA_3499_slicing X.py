import sys
sys.stdin = open("input.txt", "r")

result = []
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
    res = ''
    for i in range(t - is_odd):
        res += word[i] + ' ' + word[t + i] + ' '
    if is_odd:
        res += word[t - 1]
    result.append(res)

for test_case in range(1, T + 1):
    print('#{} {}'.format(test_case, result[test_case - 1]))