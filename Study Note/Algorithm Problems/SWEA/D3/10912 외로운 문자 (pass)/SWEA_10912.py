import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    print('#', end='')
    print(test_case, end=' ')

    word = input()
    
    count = [0] * 26
    for c in word:
        index = ord(c) - ord('a')
        count[index] += 1

    result = []
    for i in range(len(count)):
        if count[i] % 2:
            result.append(chr(i + ord('a')))
    if len(result):
        for i in result:
            print(i, end='')
        print()
    else:
        print('Good')

