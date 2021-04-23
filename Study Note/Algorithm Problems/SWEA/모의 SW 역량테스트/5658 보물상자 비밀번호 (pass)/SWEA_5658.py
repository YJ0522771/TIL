import sys
sys.stdin = open("input.txt", "r")

X_to_D = {
    '0': 0, '1': 1, '2': 2, '3': 3,
    '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'A': 10, 'B': 11,
    'C': 12, 'D': 13, 'E': 14, 'F': 15
}
T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////
    N, K = map(int, input().split())
    box = list(input())
    digit = N // 4
    nums = set({})

    for _ in range(digit):
        for i in range(0, N, digit):
            temp = 0
            for j in range(digit):
                temp *= 16
                temp += X_to_D.get(box[i + j])
            nums.add(temp)

        temp = box.pop()
        box = [temp] + box

    nums = list(nums)
    nums.sort(reverse=True)
    print('#{} {}'.format(test_case, nums[K - 1]))