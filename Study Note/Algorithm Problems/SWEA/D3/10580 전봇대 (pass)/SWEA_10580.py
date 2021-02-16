import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    wires = []
    for i in range(N):
        wires.append(tuple(map(int, input().split())))
    count = 0
    for i in range(N):
        for j in range(i, N):
            if wires[i][0] > wires[j][0] and wires[i][1] < wires[j][1]:
                count += 1
            elif wires[i][0] < wires[j][0] and wires[i][1] > wires[j][1]:
                count += 1
    print('#{} {}'.format(test_case, count))
