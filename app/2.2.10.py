n = int(input())
otvet = []
for i in range(1, n+1):
    s = input()
    if (s.find('a') < s.find('n', s.find('a')+1) < s.find('t', s.find('n')+1)
        < s.find('o', s.find('t')+1) < s.rfind('n')):
        if s.find('a') != -1 and s.find('n') != -1 and s.find('t') != -1 and s.rfind('o') != -1:
            otvet.append(i)
print(*otvet)