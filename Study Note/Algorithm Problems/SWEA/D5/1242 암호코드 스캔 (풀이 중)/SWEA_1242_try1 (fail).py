import sys
sys.stdin = open("1242_input.txt", "r")
# sys.stdout = open("out.txt", "w")

d_rate = [[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2],
          [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]]
X_to_B = {
    '1': '0001', '2': '0010', '3': '0011', '4': '0100',
    '5': '0101', '6': '0110', '7': '0111', '8': '1000',
    '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100',
    'D': '1101', 'E': '1110', 'F': '1111', '0': '0000'
}
digit = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

# for i in range(7):
#     d = []
#     for j in range(10):
#         t = ''
#         t += '0' * (d_rate[j][0] * (i + 1))
#         t += '1' * (d_rate[j][1] * (i + 1))
#         t += '0' * (d_rate[j][2] * (i + 1))
#         t += '1' * (d_rate[j][3] * (i + 1))
#         d.append(t)
#     digit.append(d)


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
    code_X = []
    code_start = []
    code_end = []
    # nums = []
    # for _ in range(N):
    #     nums.append(input())

    # 암호 추출

    # for i in range(N):
    #     j = 0
    #     while j < M:
    #         if nums[i][j] != '0':
    #             if j in code_start:     # 이미 저장한 암호면
    #                 j = code_end[code_start.index(j)] + 1
    #                 continue
    #             start = j
    #             k = M - 1
    #             while k > start:
    #                 if nums[i][k] != '0':
    #                     if k not in code_end:   # 암호 두 개가 겹쳐서 존재할 경우, 이미 한 번 끝점을 찾은 암호는 스킵
    #                         end = k
    #                         break
    #                     else:
    #                         k = code_start[code_end.index(k)] - 1
    #                 else:
    #                     k -= 1
    #             if k >= start:
    #                 code_start.append(start)
    #                 code_end.append(end)
    #                 code_X.append(nums[i][start: end + 1])
    #                 j = end + 1
    #                 continue
    #         j += 1

    last = input()
    for _ in range(N - 1):
        current = input()
        if last != current and current.count('0') != M:
            for i in range(M):
                if last[i] != current[i] and current[i] != '0':
                    start = i
                    break
            for i in range(M - 1, start - 1, -1):
                if last[i] != current[i] and current[i] != '0':
                    end = i
                    break
            temp = current[start: end + 1]
            temp = temp.strip('0')
            if '0000' in temp:
                while '0000' in temp:
                    remove_index = temp.index('0000')
                    code_X.append(temp[:remove_index])
                    for i in range(remove_index, len(temp)):
                        if temp[i] != '0':
                            break
                    temp = temp[i:]
                if len(temp):
                    code_X.append(temp)
            elif len(temp):
                code_X.append(temp)
            last = current
        elif current.count('0') == len(current):
            last = current

    # 중복 추출 제거 & 확장이 5이상 된 코드를 분할
    temp = []
    for code in code_X:
        if code not in temp:
            if len(code) < 75:
                temp.append(code)
            elif '000' in code:
                # print(code)
                while '000' in code:
                    remove_index = code.index('000')
                    temp.append(code[:remove_index])
                    for i in range(remove_index, len(code)):
                        if code[i] != '0':
                            break
                    code = code[i:]
                if len(code):
                    temp.append(code)

    code_X = temp

    # if test_case != 19:
    #     continue

    # for c in code_X:
    #     print(c)
    # print(len(code_X[53]))
    # code_X = [code_X[12]]
    # print(max([len(i) for i in code_X]))

    # 16진수 > 2진수
    code_B = []
    for code in code_X:
        temp = ''
        for c in code:
            temp += X_to_B.get(c)
        temp = temp.strip('0')
        # print(temp)
        r = len(temp) % 7
        if r:
            if temp[:r] == ('0' * r):
                temp = temp[r:]
            else:
                temp = ('0' * (7 - r)) + temp
        if len(temp) % 56:
            r = len(temp) % 56
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
        else:
            print(code_X.index(code))
            print(code)
        #     print(temp)
        #     print(temp2)


    # print(len(code_B))
    # for code in code_B:
    #     print(code)
    # print(max(code_len))

    res = 0
    # print(len(code_B))
    for i in range(len(code_B)):
        code_n = code_to_num(code_B[i])
        code_n.reverse()
        # print(sum(code_n))
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

