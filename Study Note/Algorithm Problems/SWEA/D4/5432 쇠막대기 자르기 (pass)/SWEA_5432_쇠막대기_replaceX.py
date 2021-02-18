import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////
    arr = input()

    index = 0
    count = 0
    i = 0
    while i < len(arr):
        if arr[i] == '(':
            if i < len(arr) - 1 and arr[i + 1] == ')':
                count += index
                i += 2
            else:
                index += 1
                i += 1
        else:
            index -= 1
            count += 1
            i += 1

    print('#{} {}'.format(test_case, count))
