import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////
    info = input()
    N = len(info)
    mark = {'S': 0, 'D': 1, 'H': 2, 'C': 3}
    card = [[0] * 13 for _ in range(4)]

    error = False
    for i in range(0, N, 3):
        if not card[mark.get(info[i])][int(info[i + 1 : i + 3]) - 1]:
            card[mark.get(info[i])][int(info[i + 1: i + 3]) - 1] += 1
        else:
            error = True
            break

    if error:
        result = ' ERROR'
    else:
        result = ''
        for i in range(4):
            result += ' ' + str(13 - sum(card[i]))

    print('#{}{}'.format(test_case, result))
