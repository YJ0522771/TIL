import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    res = 0
    for b in B:
        left = 0
        right = N - 1
        mid = (left + right) // 2
        if A[mid] > b:
            right = mid - 1
            last = 'l'
        elif A[mid] < b:
            left = mid + 1
            last = 'r'
        else:
            print(b)
            res += 1
            continue
        while left <= right:
            mid = (left + right) // 2
            if A[mid] > b:
                right = mid - 1
                cur = 'l'
            elif A[mid] < b:
                left = mid + 1
                cur = 'r'
            else:
                print(b)
                res += 1
                break
            if last == cur:
                break
            last = cur

    print('#{} {}'.format(test_case, res))