import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////////////////
    L = int(input())
    string = input()

    # 홀수일 경우
    if L % 2:
        print('#{} -1'.format(test_case))
        continue

    # 올바른 부분 문자열 제거
    # A파트 인덱스 저장
    A = []
    # B파트 인덱스 저장
    B = []
    for i in range(L):
        if string[i] == '(':
            B.append(i)
        elif len(B) == 0:
            A.append(i)
        else:
            B.pop()

    # A, B 모두 없음 = 처음부터 올바른 문자열
    # 테스트 케이스 중 이 경우는 없는 듯하다.
    if len(A) + len(B) == 0:
        print('#{} 0'.format(test_case))

    # B파트만 있을 경우
    if len(A) == 0:
        print('#{} 1'.format(test_case))
        print('{} {}'.format(B[len(B) // 2], B[-1]))
        continue
    # A파트만 있을 경우
    elif len(B) == 0:
        print('#{} 1'.format(test_case))
        print('{} {}'.format(A[0], A[len(A) // 2 - 1]))
        continue

    # A파트 B파트 모두 존재할 때
    # 14번 19번 test case 가 이거 (20번은 모름)
    # A파트를 먼저 바꿀 지, B파트를 먼저 바꿀 지 순서는 채점에 상관 없다.
    print('#{} 2'.format(test_case))
    start = A[0]
    end = A[-1]
    temp = []
    for i in range(len(A) - 1, -1, -1):
        temp.append((start + end) - A[i])
    A = temp
    A += B

    print('{} {}'.format(start, end))
    print('{} {}'.format(A[len(A) // 2], A[-1]))



