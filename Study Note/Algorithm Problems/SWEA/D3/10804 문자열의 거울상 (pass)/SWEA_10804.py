import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    word = input()
    result = []

    for i in range(len(word) - 1, -1, -1):
        if word[i] == 'p':
            result.append('q')
        elif word[i] == 'q':
            result.append('p')
        elif word[i] == 'b':
            result.append('d')
        elif word[i] == 'd':
            result.append('b')

    print('#{}'.format(test_case), end=' ')
    for i in result:
        print(i, end='')
    print()
