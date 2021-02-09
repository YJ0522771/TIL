import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
sys.stdin = open("SWEA_10966_sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    print('#{}'.format(test_case), end=' ')

    N, M = map(int, input().split())
    WL_map = []
    for i in range(N):
        WL_map += [input()]

    count = []
    location = []
    for i in range(N):
        count.append([])
        for j in range(M):
            if WL_map[i][j] == 'W':
                count[i] += [0]
                location += [(i, j)]
            else:
                count[i] += [-1]
    loop = True
    loop_num = 1
    while loop:
        temp = []
        for item in location:
            if item[0] > 0:
                if count[item[0] - 1][item[1]] == -1:
                    count[item[0] - 1][item[1]] = loop_num
                    temp += [(item[0] - 1, item[1])]
            if item[0] < N-1:
                if count[item[0] + 1][item[1]] == -1:
                    count[item[0] + 1][item[1]] = loop_num
                    temp += [(item[0] + 1, item[1])]
            if item[1] > 0:
                if count[item[0]][item[1] - 1] == -1:
                    count[item[0]][item[1] - 1] = loop_num
                    temp += [(item[0], item[1] - 1)]
            if item[1] < M-1:
                if count[item[0]][item[1] + 1] == -1:
                    count[item[0]][item[1] + 1] = loop_num
                    temp += [(item[0], item[1] + 1)]
        location = temp
        loop_num += 1
        for i in range(N):
            if count[i].count(-1) != 0:
                i = -1
                break
        if i != -1:
            loop = False
    result = 0
    for i in count:
        result += sum(i)
    print(result)
