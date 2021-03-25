import sys
from queue import PriorityQueue

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    res = '#{}'.format(test_case)
    heap = PriorityQueue()
    for _ in range(N):
        oper = list(map(int, input().split()))
        if oper[0] == 1:
            heap.put(oper[1] * -1)
        else:
            if not heap.empty():
                res += ' {}'.format(heap.get() * -1)
            else:
                res += ' -1'
    print(res)