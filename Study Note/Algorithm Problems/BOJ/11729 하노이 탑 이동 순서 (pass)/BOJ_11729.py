def solve(n, f, t):
    if n == 1:
        print('{} {}'.format(f, t))
        return
    
    for i in range(1, 4):
        if i != f and i != t:
            m = i
            break

    solve(n - 1, f, m)
    print('{} {}'.format(f, t))
    solve(n - 1, m, t)
    return

N = int(input())
print((1 << N) - 1)
solve(N, 1, 3)
    