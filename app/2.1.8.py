def xz(n, k):
    if n == 1:
        return 1
    else:
        return (xz(n-1, k)+ k - 1)% n +1
n, k = int(input()), int(input())
print(xz(n, k))