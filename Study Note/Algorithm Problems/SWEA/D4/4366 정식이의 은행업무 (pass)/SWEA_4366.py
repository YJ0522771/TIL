import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////
    in1 = list(map(int, list(input())))
    in2 = list(map(int, list(input())))
    in1.reverse()
    in2.reverse()

    nums = []
    for i in range(len(in1)):
        temp = 0
        t = 1
        for j in range(len(in1)):
            if j == i:
                temp += ((in1[j] + 1) % 2) * t
            else:
                temp += in1[j] * t
            t *= 2
        if temp not in nums:
            nums.append(temp)

    is_end = False
    for i in range(len(in2)):
        for k in range(1, 3):
            temp = 0
            t = 1
            for j in range(len(in2)):
                if j == i:
                    temp += ((in2[j] + k) % 3) * t
                else:
                    temp += in2[j] * t
                t *= 3
            if temp in nums:
                is_end = True
                break
        if is_end:
            break

    print('#{} {}'.format(test_case, temp))