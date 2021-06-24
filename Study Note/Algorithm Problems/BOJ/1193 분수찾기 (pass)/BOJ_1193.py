N = int(input())
s = 0
i = 1
while s < N:
    s += i
    i += 1

if i % 2:
    print('{}/{}'.format(i - (s - N + 1), s - N + 1))
else:
    print('{}/{}'.format(s - N + 1, i - (s - N + 1)))