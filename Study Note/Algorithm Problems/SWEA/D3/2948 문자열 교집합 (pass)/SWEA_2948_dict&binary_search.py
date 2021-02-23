import sys
sys.stdin = open("input.txt", "r")
# 사용 X /////////////////////////////
def binary_search(L, s):
    left = 0
    right = len(L) - 1
    while left <= right:
        mid = (left + right) // 2
        if L[mid] == s:
            return True
        if L[mid] > s:
            right = mid - 1
        else:
            left = mid + 1
    return False
# ////////////////////////////////////
T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    A = list(input().split())
    B = list(input().split())
    B_dict = {}
    for b in B:
        if B_dict.get(b[0]) == None:
            B_dict[b[0]] = [b]
        else:
            B_dict.get(b[0]).append(b)
    for i in range(ord('a'), ord('z') + 1):
        if B_dict.get(chr(i)) != None:
            B_dict.get(chr(i)).sort()
    count = 0
    for a in A:
        temp = B_dict.get(a[0])
        if temp == None:
            continue
        else:
            state = False
            left = 0
            right = len(temp) - 1
            while left <= right:
                mid = (left + right) // 2
                if temp[mid] == a:
                    state = True
                    break
                if temp[mid] > a:
                    right = mid - 1
                else:
                    left = mid + 1
            if state:
                count += 1
    # for a in A:
    #     state = False
    #     left = 0
    #     right = M - 1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if B[mid] == a:
    #             state = True
    #             break
    #         if B[mid] > a:
    #             right = mid - 1
    #         else:
    #             left = mid + 1
    #     if state:
    #         count += 1

    print('#{} {}'.format(test_case, count))
