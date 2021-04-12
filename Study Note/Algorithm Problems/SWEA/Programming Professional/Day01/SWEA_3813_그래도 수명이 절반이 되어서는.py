import sys
sys.stdin = open("input.txt", "r")


# Parametric search
def search(x):
    count = 0
    j = 0
    for i in range(1, len(W)):
        if W[i] <= x:
            count += 1
            if count == S[j]:
                j += 1
                count = 0
                if j >= len(S):
                    break
        else:
            count = 0
    if j < len(S):
        return False
    return True


T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////
    N, K = map(int, input().split())
    W = [0] + list(map(int, input().split()))
    S = list(map(int, input().split()))

    # Binary search
    left = 1
    right = 200000
    while left <= right:
        mid = (left + right) // 2
        res = search(mid)
        if res:
            right = mid - 1
        else:
            left = mid + 1
    
    if res:
        print('#{} {}'.format(test_case, mid))
    else:
        print('#{} {}'.format(test_case, mid + 1))
