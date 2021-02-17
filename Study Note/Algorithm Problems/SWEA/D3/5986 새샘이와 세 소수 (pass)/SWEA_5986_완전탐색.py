import sys
sys.stdin = open("input.txt", "r")

prime = []
for i in range(1, 1000):
    if i == 1:
        continue
    for j in range(2, i + 1):
        if j == i:
            prime += [i]
        if i % j == 0:
            break
T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    count = 0
    for i in range(len(prime)):
        if prime[i] > N:
            break
        for j in range(i, len(prime)):
            temp = N - prime[i] - prime[j]
            if temp in prime[j:]:
                count += 1
    print('#{} {}'.format(test_case, count))