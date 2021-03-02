import sys
sys.stdin = open("1242_input.txt", "r")

d_rate = [[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2],
          [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]]
X_to_B = {
    '1': '0001', '2': '0010', '3': '0011', '4': '0100',
    '5': '0101', '6': '0110', '7': '0111', '8': '1000',
    '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100',
    'D': '1101', 'E': '1110', 'F': '1111', '0': '0000'
}
digit = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']


def code_to_num(code):
    code_n = []
    for i in range(len(code) - 1, -1, -7):
        t = code[i - 6: i + 1]
        if t in digit:
            code_n.append(digit.index(t))
        else:
            return code_n
    return code_n


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

    # 암호 추출
    code_X = []
    last = '0' * M
    for n in nums:
        current = n
        if last != current:
            temp = ''
            for i in range(M):
                if last[i] != current[i]:
                    start = i
                    break
            for i in range(M - 1, start - 1, -1):
                if last[i] != current[i]:
                    end = i
                    break
            temp = last[start: end + 1].strip('0')
            if len(temp):
                for c in code_X:
                    if c != temp and c in temp:
                        temp = (temp[:temp.index(c)] + temp[temp.index(c) + len(c):]).strip('0')
                        # print(temp)
            if len(temp) and temp not in code_X:
                state = True
                for c in code_X:
                    if c != temp and temp in c:
                        state = False
                        code_X.remove(c)
                        if temp not in code_X:
                            code_X.append(temp)
                        t = c[:c.index(temp)].strip('0')
                        if len(t) and t not in code_X:
                            code_X.append(t)
                        t = c[c.index(temp) + len(temp):].strip('0')
                        if len(t) and t not in code_X:
                            code_X.append(t)
                        break
                if state:
                    while '0000' in temp:
                        code_X.append(temp[:temp.index('0000')])
                        temp = temp[temp.index('0000'):].strip('0')
                    if len(temp):
                        code_X.append(temp)
            temp = current[start: end + 1].strip('0')
            if len(temp):
                for c in code_X:
                    if c != temp and c in temp:
                        temp = (temp[:temp.index(c)] + temp[temp.index(c) + len(c):]).strip('0')
                if temp not in code_X:
                    code_X.append(temp)
            last = current

    remove_list = []
    for c in code_X:
        for j in range(len(code_X)):
            if c in code_X[j] and c != code_X[j]:
                # print(c, code_X[j])
                if code_X[j] not in remove_list:
                    remove_list.append(code_X[j])
    for r in remove_list:
        code_X.remove(r)

    # 16진수 > 2진수
    code_B = []
    for code in code_X:
        temp = ''
        for c in code:
            temp += X_to_B.get(c)
        temp = temp.strip('0')
        r = len(temp) % 56
        if r:
            temp = ('0' * (56 - r)) + temp

        r = len(temp) // 56
        state = True
        if r > 1:
            to0 = '0' * r
            to1 = '1' * r
            temp2 = ''
            for i in range(len(temp) - 1, -1, -r):
                if temp[i - r + 1: i + 1] == to0:
                    temp2 += '0'
                elif temp[i - r + 1: i + 1] == to1:
                    temp2 += '1'
                else:
                    state = False
                    break
            temp = temp2[::-1]
        if state:
            code_B.append(temp)

    # for code in code_B:
    #     print(code)

    res = 0
    for i in range(len(code_B)):
        code_n = code_to_num(code_B[i])
        code_n.reverse()
        if len(code_n) == 8:
            s = 0
            for j in range(0, 7, 2):
                s += code_n[j]
            s *= 3
            for j in range(1, 8, 2):
                s += code_n[j]
            if not s % 10:
                # print(s)
                res += sum(code_n)
    print('#{} {}'.format(test_case, res))