import sys
sys.stdin = open("input.txt", "r")

num_dic = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
keys = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////////////
    print('#{}'.format(test_case))
    t, N = input().split()
    N = int(N)
    key_input = list(input().split())
    nums = []
    for k in key_input:
        nums.append(num_dic[k])
    count = [0] * 10
    for n in nums:
        count[n] += 1
    for i in range(10):
        for _ in range(count[i]):
            print(keys[i], end=' ')
    print()