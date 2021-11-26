n = int(input())
first = 0
second = 0
third = 0
fourth = 0
for i in range(n):
    s = [i for i in input().split()]
    if int(s[0]) > 0 and int(s[1]) > 0:
        first += 1
    elif int(s[0]) > 0 and int(s[1]) < 0:
        fourth += 1
    elif int(s[0]) < 0 and int(s[1]) < 0:
        third += 1
    elif int(s[0]) < 0 and int(s[1]) > 0:
        second += 1
print('Первая четверть:', first)
print('Вторая четверть:', second)
print('Третья четверть:', third)
print('Четвертая четверть:', fourth)