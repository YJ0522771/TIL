p_bool = [True] * 1000001
p_bool[0] = p_bool[1] = False
for i in range(2, 1000001):
    if p_bool[i]:
        print(i, end=' ')
        for j in range(i * 2, 1000001, i):
            p_bool[j] = False
print()