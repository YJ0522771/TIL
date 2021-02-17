import sys
sys.stdin = open("input.txt", "r")

month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = [3, 4, 5, 6, 0, 1, 2]
T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    m, d = map(int, input().split())
    days = d
    for i in range(1, m):
        days += month[i]
    print('#{} {}'.format(test_case, week[days % 7]))