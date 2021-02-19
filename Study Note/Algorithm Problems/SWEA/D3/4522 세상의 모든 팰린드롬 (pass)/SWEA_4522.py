import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////////////////////
    word = input()
    N = len(word)
    state = True
    for i in range(N // 2):
        if word[i] != word[N - 1 - i] and word[N - 1 - i] != '?' and word[i] != '?':
            state = False
            break
    if state:
        print('#{} Exist'.format(test_case))
    else:
        print('#{} Not exist'.format(test_case))