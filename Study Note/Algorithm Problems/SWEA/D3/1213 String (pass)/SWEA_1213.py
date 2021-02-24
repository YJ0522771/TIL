# import sys
# sys.stdin = open("test_input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N = input()
    word = input()
    string = input()
    print('#{} {}'.format(N, string.count(word)))