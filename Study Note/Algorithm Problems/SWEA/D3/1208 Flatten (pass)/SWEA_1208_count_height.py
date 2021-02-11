import sys

sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    print('#{}'.format(test_case), end=' ')

    dump = int(input())
    block = list(map(int, input().split()))

    h_count = [0] * 101     # 0부터 100까지

    for i in range(100):
        h_count[block[i]] += 1

    for i in range(dump):
        for j in range(101):
            if h_count[j]:
                break
        for k in range(100, -1, -1):
            if h_count[k]:
                break
        h_count[j] -= 1
        h_count[j + 1] += 1
        h_count[k] -= 1
        h_count[k - 1] += 1
    
    for j in range(101):
        if h_count[j]:
            break
    for k in range(100, -1, -1):
        if h_count[k]:
            break

    print(k - j)
