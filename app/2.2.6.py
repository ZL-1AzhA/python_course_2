n = int(input())
z = 1
s = [int(input()) for i in range(n)]
num = int(input())
for i in range(n):
    for j in range(i+1, n):
        if s[i]*s[j] == num:
            z = 0
if z == 0:
    print('ДА')
else:
    print('НЕТ')