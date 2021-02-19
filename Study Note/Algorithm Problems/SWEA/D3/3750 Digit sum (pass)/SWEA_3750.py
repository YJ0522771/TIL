import sys
sys.stdin = open("input.txt", "r")

res = []
T = int(input())
for test_case in range(1, T + 1):
    # ////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////////////////////////
    n = input()

    while len(n) > 1:
        s = 0
        for i in n:
            s += int(i)
        n = str(s)
    res.append(n)

for test_case in range(1, T + 1):
    print('#{} {}'.format(test_case, res[test_case - 1]))