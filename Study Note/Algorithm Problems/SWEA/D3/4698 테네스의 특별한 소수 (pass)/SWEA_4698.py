import sys
sys.stdin = open("input.txt", "r")

p_bool = [True] *1000001
p_bool[0] = p_bool[1] = False
prime = []
for i in range(2, 1000001):
    if p_bool[i]:
        prime.append(i)
    for j in range(i * 2, 1000001, i):
        p_bool[j] = False

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    D, A, B = map(int, input().split())
    D = str(D)
    count = 0
    for i in prime:
        if i < A:
            continue
        elif i > B:
            break
        if D in str(i):
            count += 1
    print('#{} {}'.format(test_case, count))