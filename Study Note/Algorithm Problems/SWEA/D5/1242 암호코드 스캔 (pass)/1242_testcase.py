import sys
sys.stdin = open("1242_input.txt", "r")
sys.stdout = open("1242_input_18.txt", "w")

T = int(input())
for test_case in range(1, T + 1):
    # test case 추출

    N, M = map(int, input().split())
    nums = []
    for _ in range(N):
        nums.append(input())

    if test_case != 18:
        continue

    print(1)
    print('{} {}'.format(N, M))
    for n in nums:
        print(n)