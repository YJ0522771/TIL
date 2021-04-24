import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////////
    N, M, K, A, B = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t = list(map(int, input().split()))

    visit = [[0, 0] for _ in range(K + 1)]      # 손님이 방문한 창구 번호
    a_state = [[0] * len(a) for _ in range(2)]  # 접수 창구 상태 [[손님 번호], [남은 시간]]
    b_state = [[0] * len(b) for _ in range(2)]  # 졍비 창구 상태
    # print(a_state)
    time = 0
    k = 1               # 손님 번호
    a_queue = []        # 접수 창구 대기 손님
    b_queue = []        # 정비 창구 대기 손님
    count = 0           # 정비 완료 손님 수
    while count < K:
        while len(t) and t[0] == time:
            t.pop(0)
            a_queue.append(k)
            k += 1

        # 접수 창구
        for i in range(len(a)):
            # 해당 창구에 손님이 있는 경우 : 남은 시간을 1 줄임
            if a_state[1][i] > 0:
                a_state[1][i] -= 1

            # 남은 시간이 0이 되면
            if a_state[1][i] == 0:
                # 손님이 있던 곳이 끝난 거면 정비 창구 대기열로 이동.
                # 창구를 비운다.
                if a_state[0][i]:
                    b_queue.append(a_state[0][i])
                    a_state[0][i] = 0
                # 접수 창구 대기열에 손님이 있으면 해당 창구에 배치
                if len(a_queue):
                    p = a_queue.pop(0)
                    a_state[0][i] = p
                    visit[p][0] = i + 1     # 방문한 접수 창구 번호를 저장
                    a_state[1][i] = a[i]    # 남은 시간 초기화

        # 정비 창구
        for i in range(len(b)):
            # 해당 창구에 손님이 있는 경우 : 남은 시간을 1 줄임
            if b_state[1][i] > 0:
                b_state[1][i] -= 1

            # 남은 시간이 0이 되면
            if b_state[1][i] == 0:
                # 완료된 손님으로 카운트
                if b_state[0][i]:
                    count += 1
                    b_state[0][i] = 0
                # 대기열에 손님이 있으면 배치
                if len(b_queue):
                    p = b_queue.pop(0)
                    b_state[0][i] = p
                    visit[p][1] = i + 1     # 방문한 정비 창구 번호를 저장
                    b_state[1][i] = b[i]

        # print(time, a_state[0], b_state[0])
        time += 1

    # print(visit)
    res = 0
    for i in range(1, K + 1):
        if visit[i][0] == A and visit[i][1] == B:
            res += i

    print('#{} {}'.format(test_case, res if res else -1))



