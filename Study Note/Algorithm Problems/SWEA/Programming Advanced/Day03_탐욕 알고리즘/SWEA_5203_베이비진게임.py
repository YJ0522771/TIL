import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////////////////////////
    nums = list(map(int, input().split()))
    win = 0
    count = [[0] * 10 for _ in range(2)]
    for i in range(0, len(nums), 2):
        for j in range(2):
            count[j][nums[i + j]] += 1
            if 3 in count[j]:
                win = j + 1
                break
            for k in range(8):
                if count[j][k] and count[j][k + 1] and count[j][k + 2]:
                    win = j + 1
            if win:
                break
        if win:
            break
    print('#{} {}'.format(test_case, win))