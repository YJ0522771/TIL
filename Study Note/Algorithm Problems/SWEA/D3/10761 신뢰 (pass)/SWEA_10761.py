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
    inputs = list(input().split())
    N = int(inputs.pop(0))
    orders = []
    b_btn = []
    o_btn = []
    for i in range(N):
        r = inputs.pop(0)
        b = int(inputs.pop(0))
        if r == 'B':
            b_btn.append(b)
        else:
            o_btn.append(b)

        orders.append(r)

    b_cur = 1
    o_cur = 1
    count = 0
    while len(orders):
        b_act = False
        o_act = False
        if orders[0] == 'B' and b_cur == b_btn[0]:
            orders.pop(0)
            b_btn.pop(0)
            b_act = True
        elif orders[0] == 'O' and o_cur == o_btn[0]:
            orders.pop(0)
            o_btn.pop(0)
            o_act = True
        if (not o_act) and len(o_btn):
            if o_btn[0] > o_cur:
                o_cur += 1
            elif o_btn[0] < o_cur:
                o_cur -= 1
            o_act = True
        if (not b_act) and len(b_btn):
            if b_btn[0] > b_cur:
                b_cur += 1
            elif b_btn[0] < b_cur:
                b_cur -= 1
            b_act = True
        count += 1
    print('#{} {}'.format(test_case, count))