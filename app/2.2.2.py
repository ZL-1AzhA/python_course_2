s = [int(i) for i in input().split()]
s.reverse()
count = 0
for i in range(len(s)-1):
    if s[i] > s[i+1]:
        count += 1
print(count)