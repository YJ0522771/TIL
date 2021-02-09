import sys

sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    print('#{}'.format(test_case), end=' ')

    dump = int(input())
    block = list(map(int, input().split()))

    for i in range(dump):
        max_b = 0
        min_b = 0
        for k in range(1, 100):
            if block[k] > block[max_b]:
                max_b = k
            if block[k] < block[min_b]:
                min_b = k
        block[max_b] -= 1
        block[min_b] += 1

    max_b = 0
    min_b = 0
    for k in range(1, 100):
        if block[k] > block[max_b]:
            max_b = k
        if block[k] < block[min_b]:
            min_b = k
    print(block[max_b] - block[min_b])
