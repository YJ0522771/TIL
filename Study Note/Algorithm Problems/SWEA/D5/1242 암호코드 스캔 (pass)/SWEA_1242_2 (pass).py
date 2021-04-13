import sys
from datetime import datetime
sys.stdin = open("1242_input.txt", "r")

# 모두 2진수로 바꾸는게 오래 걸리는 듯하다.
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
    input_X = [input() for _ in range(N)]

    # 16진수 -> 2진수
    input_B = []
    for i in range(N):
        temp = ''
        for X in input_X[i]:
            if X in X_to_B.keys():
                temp += X_to_B.get(X)
        input_B.append(temp)

    # 코드 추출
    codes = []
    zero = '0' * (M * 4)
    last = zero
    for i in range(N):
        cur = input_B[i]
        if last == cur:
            continue

        if cur == zero:
            last = cur
            continue

        end = M * 4 - 1
        while end >= 0:
            if cur[end] == '0':
                end -= 1
                continue
            for l in range(1, 6):
                code = []
                # 암호가 늘어났을 경우의 한 숫자 당 길이 (늘어난 배수 : l)
                step = l * (-7)

                # 앞부분의 길이가 (간격 * 8)보다 짧을 경우, 해당 l은 유효하지 않으므로
                if end + (step * 8) < -1:
                    end -= 1
                    break

                for j in range(end, end + (step * 8), step):
                    # step만큼 잘라서 유효한 암호인지 검사
                    temp = cur[j + step + 1 : j + 1]
                    if temp in digit[l - 1]:
                        code.append(digit[l - 1].index(temp))
                    # 현재 검사한 구간이 유효하지 않으면 = 유효하지 않은 코드
                    else:
                        break

                # 유효한 8 숫자를 모두 얻었을 때
                if len(code) == 8:
                    code.reverse()
                    # 추출한 코드가 중복이 아닐 경우
                    if code not in codes:
                        codes.append(code)
                    # 다음 코드를 찾기 위해 코드의 길이만큼 앞으로 간다.
                    end += (step * 8)
                    break
                # 5배 길이까지 유효하지 않은 경우
                elif l == 5:
                    end -= 1
        last = cur

    # 검증코드 여부 검사
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