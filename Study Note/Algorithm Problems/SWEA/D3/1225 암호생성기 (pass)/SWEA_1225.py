import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////////
    t = int(input())
    nums = list(map(int, input().split()))
    while True:
        for i in range(1, 6):
            temp = nums.pop(0) - i
            if temp <= 0:
                nums.append(0)
                break
            else:
                nums.append(temp)

        if nums[7] == 0:
            break

    print('#{} {}'.format(test_case, ' '.join(map(str, nums))))