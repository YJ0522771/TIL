import sys
sys.stdin = open("input.txt", "r")


def is_equal(arr1, arr2):
    for i in range(26):
        if arr1[i] != arr2[i]:
            return False
    return True


T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////
    S1, S2 = input().split()

    S1_count = [0] * 26
    for s in S1:
        S1_count[ord(s) - ord('a')] += 1
    n = len(S1)

    res = 0
    S2_count = [0] * 26
    for i in range(n - 1):
        S2_count[ord(S2[i]) - ord('a')] += 1

    for i in range(len(S2) - n + 1):
        S2_count[ord(S2[i + n - 1]) - ord('a')] += 1
        if is_equal(S1_count, S2_count):
            res += 1
        S2_count[ord(S2[i]) - ord('a')] -= 1
    print('#{} {}'.format(test_case, res))