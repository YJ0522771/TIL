import sys
sys.stdin = open("input.txt", "r")

res = []
T = int(input())
for test_case in range(1, T + 1):
    # ////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////
    a, b = map(int, input().split())
    count = 0
    while not (a == 1 and b == 1):
        if b > a:
            a, b = b, a
        temp = a // b
        if a == temp * b:
            temp -= 1
        count += temp
        a -= (temp * b)
    res.append('#{} {}'.format(test_case, count))

for i in range(T):
    print(res[i])