def pibonacci(n):
    if n <=1:
        return 1
    else:
        return pibonacci(n-1) + pibonacci(n-2)

T = int(input())
for _ in range(T):
    N = int(input())
    