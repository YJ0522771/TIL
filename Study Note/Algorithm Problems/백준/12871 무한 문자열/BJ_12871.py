s = 'abc'
t = 'abcabc'

if len(s) > len(t):
    s, t = t, s
            
for i in range(len(t)):
    if t[i] == s[0]:
        break
t = t[i:] + t[:i]

len_t = len(t)
t *= 2
state = 1
for i in range(0, len_t, len(s)):
    for j in range(len(s)):
        if t[i + j] != s[j]:
            state = 0
            break
print(int(state))