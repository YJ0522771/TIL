def fac(i):
    if i == 0:
        return 1
    return i * fac(i - 1)

N = int(input())
print(fac(N))