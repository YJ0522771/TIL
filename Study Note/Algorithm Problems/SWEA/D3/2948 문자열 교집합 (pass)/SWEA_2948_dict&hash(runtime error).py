import sys
sys.stdin = open("input.txt", "r")

def hashing(s):
    key = 0
    for i in range(len(s)):
        key += ord(s[i]) * (i + 1)
    return key % 100000

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
    h_dict = {}
    for b in B:
        k = hashing(b)
        if h_dict.get(k) == None:
            h_dict[k] = [b]
        else:
            h_dict.get(k).append(b)
    count = 0
    for a in A:
        k = hashing(a)
        temp = h_dict.get(k)
        if temp != None:
            for t in temp:
                if t == a:
                    count += 1

    print('#{} {}'.format(test_case, count))
