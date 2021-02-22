import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    score = list(map(int, input().split()))
    s = 0
    for i in score:
        if i < 40:
            s += 40
        else:
            s += i
    
    print('#{} {}'.format(test_case, s // 5))