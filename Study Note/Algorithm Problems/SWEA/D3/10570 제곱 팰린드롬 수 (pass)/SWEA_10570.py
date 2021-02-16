import sys
sys.stdin = open("input.txt", "r")

def test(string):
    temp = string[::-1]
    return temp == string

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    A, B = map(int, input().split())
    count = 0
    A = int(A ** 0.5) + 1 if (A ** 0.5) % 1 else int(A ** 0.5)
    for i in range(A, B + 1):
        power = i * i 
        if power > B:
            break
        if test(str(i)) and test(str(power)):
            count += 1

    print('#{} {}'.format(test_case, count))
