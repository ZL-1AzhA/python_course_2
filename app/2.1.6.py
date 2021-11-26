n = input()
if len(n) == 5:
    print(int(n[::-1]))
elif len(n) == 6:
    print(int(n[0] + n[:-6:-1]))