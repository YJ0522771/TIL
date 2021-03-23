import sys
sys.stdin = open("input.txt", "r")


def heap_insert(num):
    global heap
    cur = len(heap)
    heap.append(num)
    while cur > 1:
        if num > heap[cur // 2]:
            heap[cur] = heap[cur // 2]
            cur //= 2
        else:
            break
    heap[cur] = num
    return


def heap_pop():
    global heap
    if len(heap) < 2:
        return -1
    elif len(heap) == 2:
        return heap.pop()
    p = heap[1]
    n = heap.pop()
    cur = 1
    while 2 * cur < len(heap):
        if 2 * cur + 1 == len(heap):
            if n < heap[2 * cur]:
                heap[cur] = heap[2 * cur]
                cur *= 2
            break

        if n < heap[2 * cur] and heap[2 * cur] >= heap[2 * cur + 1]:
            heap[cur] = heap[2 * cur]
            cur *= 2
        elif n < heap[2 * cur + 1]:
            heap[cur] = heap[2 * cur + 1]
            cur *= 2
            cur += 1
        else:
            break
    heap[cur] = n

    return p


T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    res = '#{}'.format(test_case)
    heap = [-1]
    for _ in range(N):
        oper = list(map(int, input().split()))
        if oper[0] == 1:
            heap_insert(oper[1])
        else:
            res += ' {}'.format(heap_pop())
    print(res)
