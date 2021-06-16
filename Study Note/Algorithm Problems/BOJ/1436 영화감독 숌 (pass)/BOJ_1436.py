def solve(temp):
    count = 0
    while temp > 0:
        if temp % 10 == 6:
            count += 1
        else:
            count = 0
        temp //= 10
        if count == 3:
            return True
    return False


N = int(input())
res = []
for i in range(100, 3000000):
    if solve(i):
        res.append(i)
    if len(res) == N:
        break

print(res[N - 1])