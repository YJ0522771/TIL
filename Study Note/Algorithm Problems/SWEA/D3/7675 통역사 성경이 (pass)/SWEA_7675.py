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
    words = list(input().split())
    end = ['.', '?', '!']
    count = [0] * N
    index = 0
    for w in words:
        upper = 0
        lower = 0
        for c in w:
            upper += c.isupper()
            lower += c.islower()
        if upper == 1 and w[0].isupper and end.count(w[-1]) + upper + lower == len(w):
            count[index] += 1
        # elif lower == len(w) - 1 and end.count(w[-1]):
        #     count[index] += 1

        if end.count(w[-1]):
            index += 1
    print('#{}'.format(test_case), end='')
    for i in count:
        print(' {}'.format(i), end='')
    print()