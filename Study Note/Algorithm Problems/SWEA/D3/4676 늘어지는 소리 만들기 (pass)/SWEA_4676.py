import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    word = list(input())
    L = len(word)
    h = int(input())
    hyphen_input = list(map(int, input().split()))
    hyphen_count = [0] * (L + 1)
    for i in hyphen_input:
        hyphen_count[i] += 1

    h_num = 0
    for i in range(L + 1):
        while hyphen_count[i]:
            word.insert(i + h_num, '-')
            h_num += 1
            hyphen_count[i] -= 1

    print('#{} {}'.format(test_case, ''.join(word)))
