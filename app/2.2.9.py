count = 0
big = 0
s = input()
for i in range(len(s)-1):
    if s[i] == s[i+1] and s[i] == 'Р':
        count += 1
    else:
        count = 0
    if count >= big:
        big = count
print(0 if s == len(s)*'О' else big+1)