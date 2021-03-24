import sys
sys.stdin = open("input.txt", "r")


def heap_insert(num):
    global heap
    global heap_end
    heap_end += 1
    cur = heap_end
    parent = cur // 2
    while parent > 0:
        if not heap[parent] < num:
            break
        heap[cur] = heap[parent]
        cur = parent
        parent = cur // 2
    heap[cur] = num
    # print('insert : {}'.format(heap[0:heap_end+1]))
    return


def heap_pop():
    global heap
    global heap_end
    if not heap_end:
        return -1
    m = heap[1]
    k = heap[heap_end]
    heap[heap_end] = -1
    heap_end -= 1
    cur = 1
    while 2 * cur < heap_end:
        if k > heap[2 * cur] and k > heap[2 * cur + 1]:
            break
        if heap[2 * cur] >= heap[2 * cur + 1]:
            child = 2 * cur
        else:
            child = 2 * cur + 1
        heap[cur] = heap[child]
        cur = child
    heap[cur] = k
    # print('pop : {}'.format(heap[0:heap_end + 1]))
    return m


T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    res = '#{}'.format(test_case)
    heap = [-1] * 100000
    heap_end = 0
    for _ in range(N):
        oper = list(map(int, input().split()))
        if oper[0] == 1:
            heap_insert(oper[1])
        else:
            res += ' {}'.format(heap_pop())
    print(res)
