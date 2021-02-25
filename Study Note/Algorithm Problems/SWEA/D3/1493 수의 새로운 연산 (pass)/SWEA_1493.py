import sys
sys.stdin = open("input.txt", "r")

to_i_sum = [0]
for i in range(1, 300):
    temp = i * (i + 1) // 2
    to_i_sum.append(temp)


def num_to_loc(n):
    for i in range(len(to_i_sum)):
        if n <= to_i_sum[i]:
            break
    return i - (to_i_sum[i] - n), 1 + (to_i_sum[i] - n)


def loc_sum(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1]


def loc_to_nums(t):
    return to_i_sum[t[0] + t[1] - 1] - (t[1] - 1)


T = int(input())
for test_case in range(1, T + 1):
    # ////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////////
    p, q = map(int, input().split())
    print(len(to_i_sum))
    print(loc_sum(num_to_loc(p), num_to_loc(q)))
    print('#{} {}'.format(test_case, loc_to_nums(loc_sum(num_to_loc(p), num_to_loc(q)))))
