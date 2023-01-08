def factorial(n):
    count = 1
    for i in range(2, n+1):
        count *= i
    return count

n, m = map(int, input().split())
print(factorial(n)//(factorial(n-m) * factorial(m)))
