# import datetime

def solve(r, c, n):
    if n == 0:
        return '*'

    if (r // n) % 3 == 1 and (c // n) % 3 == 1:
        return ' '
    else:
        return solve(r, c, n // 3)
    

N = int(input())
# start = datetime.datetime.now()
res = []
for i in range(N):
    temp = ''
    for j in range(N):
        temp += solve(i, j, N // 3)
    res.append(temp)  

for r in res:
    print(r)

# print(datetime.datetime.now() - start)