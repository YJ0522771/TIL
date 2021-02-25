import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////////////////
    N = int(input())
    visit = [False] * N
    student = []
    for _ in range(N):
        f, t = map(int, input().split())
        student.append(sorted([(f // 2) + (f % 2) - 1, (t // 2) + (t % 2) - 1]))
    corridor = [0] * 200
    for i in range(N):
        state = True
        for j in range(student[i][0], student[i][1] + 1):
            corridor[j] += 1

    print('#{} {}'.format(test_case, max(corridor)))