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
    deco1 = ''
    deco2 = ''
    word_deco = ''
    for w in word:
        deco1 += '..#.'
        deco2 += '.#.#'
        word_deco += '#.' + w + '.'
    deco1 += '.'
    deco2 += '.'
    word_deco += '#'
    print(deco1)
    print(deco2)
    print(word_deco)
    print(deco2)
    print(deco1)