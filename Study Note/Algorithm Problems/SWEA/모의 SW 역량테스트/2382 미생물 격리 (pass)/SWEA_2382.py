import sys
sys.stdin = open("input.txt", "r")


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////////////////////////
    N, M, K = map(int, input().split())

    samples = []
    for _ in range(K):
        # r, c, n, d
        samples.append(list(map(int, input().split())))
    # print(samples)

    for _ in range(M):
        for sample in samples:
            sample[0] += delta[sample[3]][0]
            sample[1] += delta[sample[3]][1]
            if sample[0] == 0 or sample[0] == N - 1 or sample[1] == 0 or sample[1] == N - 1:
                sample[2] //= 2
                # 방향 전환
                if sample[3] % 2:
                    sample[3] += 1
                else:
                    sample[3] -= 1

        samples.sort(key=lambda x: (x[0], x[1], -x[2]))
        # print(samples)

        ll = len(samples)
        new = []
        i = 0
        while i < ll:
            if i < ll - 1 and samples[i][0] == samples[i + 1][0] and samples[i][1] == samples[i + 1][1]:
                end = True
                for j in range(1, ll - i):
                    if samples[i][0] == samples[i + j][0] and samples[i][1] == samples[i + j][1]:
                        samples[i][2] += samples[i + j][2]
                    else:
                        end = False
                        break
                new.append(samples[i])
                if not end:
                    i += j
                else:
                    break
            else:
                new.append(samples[i])
                i += 1
        samples = new
        # print(new)

    res = 0
    for sample in samples:
        res += sample[2]
    print('#{} {}'.format(test_case, res))

