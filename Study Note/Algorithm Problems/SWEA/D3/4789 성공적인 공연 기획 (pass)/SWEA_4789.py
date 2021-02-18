import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    p = list(input())
    count = 0
    total = [int(p[0])]
    for i in range(1, len(p)):
        temp = i - total[i - 1]
        total.append(total[i - 1] + int(p[i]))
        if temp > 0:
            count += temp
            total[i] += temp

    print('#{} {}'.format(test_case, count))