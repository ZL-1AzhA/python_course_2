num = input()
s = []
for i in range(-1, -len(num)-1, -1):
    s.append(num[i])
    if abs(i) % 3 == 0:
        s.append(',')
s.reverse()
if s[0] == ',':
    print(*s[1:], sep='')
else:
    print(*s, sep='')