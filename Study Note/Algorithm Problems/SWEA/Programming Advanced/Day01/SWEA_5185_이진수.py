import sys
sys.stdin = open("5185_input.txt", "r")

X_to_B = {
    '1': '0001', '2': '0010', '3': '0011', '4': '0100',
    '5': '0101', '6': '0110', '7': '0111', '8': '1000',
    '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100',
    'D': '1101', 'E': '1110', 'F': '1111', '0': '0000'
}
T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////////
    N, num = input().split()
    res = ''
    for n in num:
        res += X_to_B.get(n)
    print('#{} {}'.format(test_case, res))