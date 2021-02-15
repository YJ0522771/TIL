import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    print('#{}'.format(test_case), end=' ')
    P_str = input()
    Q_str = input()

    P = []
    for c in P_str:
        if c == ' ':
            continue
        P += [c]
    
    Q = []
    for c in Q_str:
        if c == ' ':
            continue
        Q += [c]
    P += ['a']

    if ''.join(P) == ''.join(Q):
        print('N')
    else:
        print('Y')


