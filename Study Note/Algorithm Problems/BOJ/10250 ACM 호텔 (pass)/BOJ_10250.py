T = int(input())
for tc in range(T):
    H, W, N = map(int, input().split())
    X = N // H + 1
    Y = N % H
    if not Y:
        Y = H
        X -= 1
    if X < 10:
        print('{}0{}'.format(Y, X))
    else:
        print('{}{}'.format(Y, X))
