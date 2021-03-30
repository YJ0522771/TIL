A, B = map(int, input().split())
count = 1
while B > A:
    if B % 10 == 1:
        B //= 10
    elif B % 2:
        break
    else:
        B //= 2
    count += 1
if A == B:
    print(count)
else:
    print(-1)