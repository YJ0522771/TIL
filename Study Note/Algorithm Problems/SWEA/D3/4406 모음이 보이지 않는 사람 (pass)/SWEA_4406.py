import sys
sys.stdin = open("input.txt", "r")

vowel = ['a', 'e', 'i', 'o', 'u']
T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////
    word = list(input())
    result = ''
    for w in word:
        if not w in vowel:
            result += w
    print('#{} {}'.format(test_case, result))



