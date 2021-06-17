def fibo(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1

    return fibo(i - 1) + fibo(i - 2)

N = int(input())
print(fibo(N))