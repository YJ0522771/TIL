import sys
sys.stdin = open("input.txt", "r")

def in_order(cur):
    if child[cur][0]:
        in_order(child[cur][0])
    print(word[cur], end='')
    if child[cur][1]:
        in_order(child[cur][1])
    return

T = 10
for test_case in range(1, T + 1):
    # ////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////
    N = int(input())
    word = ['a']
    child = [[0] * 2]

    for _ in range(N):
        l = list(input().split())
        word.append(l[1])
        temp = [0] * 2
        if len(l) == 4:
            temp[0] = int(l[2])
            temp[1] = int(l[3])
        elif len(l) == 3:
            temp[0] = int(l[2])
        child.append(temp)

    print('#{} '.format(test_case), end='')
    in_order(1)
    print()