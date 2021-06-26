A, B, C = map(int, input().split())

if C <= B:
    print(-1)
else:
    temp = A // (C - B)
    q = A % (C - B)
    print(temp + 1)