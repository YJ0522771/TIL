s = list(input())
t = list(input())

while len(s) < len(t):
    temp = t.pop()
    if temp == 'B':
        t.reverse()
if ''.join(s) == ''.join(t):
    print(1)
else:
    print(0)