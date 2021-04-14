import sys
sys.stdin = open("input.txt", "r")


def solve(cur):
    global nums
    global ww
    if cur == K:
        return
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue

            nums[i], nums[j] = nums[j], nums[i]
            temp = int(''.join(nums))
            cur_odd = (cur + 1) % 2
            if cur_odd == K_odd:
                if temp in ww:
                    nums[i], nums[j] = nums[j], nums[i]
                    continue
                ww.append(temp)
            solve(cur + 1)
            nums[i], nums[j] = nums[j], nums[i]


T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////
    nums, K = input().split()
    K = int(K)
    K_odd = K % 2
    nums = list(nums)

    # 한 번 등장하고 나면 2 깊이마다 반복해서 나타난다.
    # K의 홀짝에 의해 결정되므로
    # 홀수 깊이에서 나타날 경우와 짝수 깊이에서 나타날 경우를 따로 고려해주어야한다.
    ww = []
    if not K_odd:
        ww.append(int(''.join(nums)))
    solve(0)

    res = 0
    for w in ww:
        if res < w:
            res = w
    print('#{} {}'.format(test_case, res))
