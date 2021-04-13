import sys
from datetime import datetime
sys.stdin = open("1242_input.txt", "r")

start_time = datetime.now()

d_rate = [[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2],
          [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]]
X_to_B = {
    '1': '0001', '2': '0010', '3': '0011', '4': '0100',
    '5': '0101', '6': '0110', '7': '0111', '8': '1000',
    '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100',
    'D': '1101', 'E': '1110', 'F': '1111', '0': '0000'
}
digit = []
for i in range(5):
    d = []
    for j in range(10):
        t = ''
        t += '0' * (d_rate[j][0] * (i + 1))
        t += '1' * (d_rate[j][1] * (i + 1))
        t += '0' * (d_rate[j][2] * (i + 1))
        t += '1' * (d_rate[j][3] * (i + 1))
        d.append(t)
    digit.append(d)

T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    nums = []
    for _ in range(N):
        nums.append(input())

    codes = []
    zero = '0' * M
    last = zero
    for n in range(N):
        current = nums[n]
        if last != current:
            if current == zero:
                last = current
                continue
            ################## Runtime error ################## 입력에 공백이나 16진수 이외의 문자가 들어가는 듯하다.
            temp = ''
            for c in current:
                if c in X_to_B.keys():
                    temp += X_to_B.get(c)
            ###################################################
            end = len(temp) - 1
            while end >= 0:
                if temp[end] == '0':
                    end -= 1
                    continue
                for l in range(1, 6):
                    code = []
                    term = -7 * l
                    if end + (term * 8) < -1:
                        end -= 1
                        break
                    for j in range(end, end + (term * 8), term):
                        state = False
                        for x in range(10):
                            if temp[j + term + 1: j + 1] == digit[l - 1][x]:
                                code.append(x)
                                state = True
                                break
                        if not state:
                            break
                    if len(code) == 8:
                        code.reverse()
                        if code not in codes:
                            codes.append(code)
                        end += (term * 8)
                        break
                    elif l == 5:
                        end -= 1
            last = current

    res = 0
    for code in codes:
        s = 0
        for j in range(0, 7, 2):
            s += code[j]
        s *= 3
        for j in range(1, 8, 2):
            s += code[j]
        if not s % 10:
            res += sum(code)
    print('#{} {}'.format(test_case, res))

print(datetime.now() - start_time)

