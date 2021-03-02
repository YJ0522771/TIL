# test case 별로 파일 생성하는 코드
import sys
sys.stdin = open("1242_input.txt", "r")

# 원하는 test case 번호
CASE = 18
sys.stdout = open("1242_input_{}.txt".format(CASE), "w")

T = int(input())
for test_case in range(1, T + 1):
    # test case 추출
    
    N, M = map(int, input().split())
    nums = []
    for _ in range(N):
        nums.append(input())

    if test_case != CASE:
        continue

    print(1)
    print('{} {}'.format(N, M))
    for n in nums:
        print(n)