import sys
sys.stdin = open("input.txt", "r")


def heap_push(e):
    global heap
    heap[0] += 1
    heap.append(e)
    child = heap[0]
    while child // 2 > 0:
        parent = child // 2
        if heap[parent][2] > e[2]:
            heap[child] = heap[parent]
            child = parent
        else:
            break
    heap[child] = e
    return


def heap_pop():
    global heap
    if heap[0] == 0:
        return
    ret = heap[1]
    heap[1] = heap[heap[0]]
    heap[0] -= 1
    heap.pop()
    parent = 1
    while parent * 2 <= heap[0]:
        child = parent * 2
        if child + 1 <= heap[0] and heap[child][2] > heap[child + 1][2]:
            child += 1

        if heap[child][2] < heap[parent][2]:
            heap[child], heap[parent] = heap[parent], heap[child]
            parent = child
        else:
            break
    return ret


T = int(input())
for test_case in range(1, T + 1):
    # ////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////////////////////////
    N = int(input())
    M = int(input())
    ee = [tuple(map(int, input().split())) for _ in range(M)]
    edges = {}
    for i in range(1, N + 1):
        edges[i] = []
    for e in ee:
        edges[e[0]].append((e[0], e[1], e[2]))
        edges[e[1]].append((e[1], e[0], e[2]))

    heap = [0]
    visit = [False] * (N + 1)
    visit[1] = True
    for e in edges[1]:
        heap_push(e)

    count = 0
    res = 0
    while count < N - 1 and heap[0]:
        temp = heap_pop()

        if visit[temp[0]] and visit[temp[1]]:
            continue

        count += 1
        res += temp[2]
        if visit[temp[0]]:
            a = temp[1]
        else:
            a = temp[0]

        for e in edges[a]:
            if visit[e[1]]:
                continue
            heap_push(e)
        visit[a] = True

    print('#{} {}'.format(test_case, res))