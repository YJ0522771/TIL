import sys
sys.stdin = open("input.txt", "r")

digit = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    last_i = -2
    nums = []
    for _ in range(N):
        nums.append(input())

    for j in range(N):
        for i in range(M - 1, -1, -1):
            if nums[j][i] == '1':
                last_i = i
                break
        if last_i != -2:
            break
    
    code = []
    for i in range(last_i, last_i - 56, -7):
        temp = nums[j][i - 6 : i + 1]
        if temp in digit:
            code.append(digit.index(temp))
        else:
            break
    
    if len(code) != 8:
        print('#{} 0'.format(test_case))
        continue
    
    code.reverse()
    s = 0
    for i in range(0, 7, 2):
        s += code[i]
    s *= 3
    for i in range(1, 8, 2):
        s += code[i]
    
    if s % 10:
        print('#{} 0'.format(test_case))
    else:
        print('#{} {}'.format(test_case, sum(code)))

    # print(code)