import sys
sys.stdin = open("input.txt", "r")


def solve(cur):
    if tree[cur] in oper:
        a = solve(child[cur][0])
        b = solve(child[cur][1])
        if tree[cur] == '+':
            return a + b
        elif tree[cur] == '-':
            return a - b
        elif tree[cur] == '*':
            return a * b
        else:
            return a / b
    else:
        return tree[cur]


oper = ['+', '-', '*', '/']
T = 10
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////////////////
    N = int(input())
    tree = [0]
    child = [[0] * 2 for _ in range(N + 1)]
    for _ in range(N):
        l = list(input().split())
        if l[1] in oper:
            tree.append(l[1])
            child[int(l[0])][0] = int(l[2])
            child[int(l[0])][1] = int(l[3])
        else:
            tree.append(int(l[1]))

    print('#{} {}'.format(test_case, int(solve(1))))