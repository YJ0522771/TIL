import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    words = []
    state = [1, 1, 1, 1, 1]
    for _ in range(5):
        words.append(input())
    result = ''
    for i in range(15):
        for j in range(5):
            if state[j]:
                result += words[j][i]
                if i + 1 >= len(words[j]):
                    state[j] -= 1
    print('#{} {}'.format(test_case, result))