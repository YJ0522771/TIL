N = int(input())

W = []
H = []
res = [1] * N
for _ in range(N):
    a, b = map(int, input().split())
    W.append(a)
    H.append(b)

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if W[i] < W[j] and H[i] < H[j]:
            res[i] += 1

for r in res:
    print(r, end=' ')
print()