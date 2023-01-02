N, K = map(int, input().split())
count = 0
while N > 2 ** count:
    a = N // (2**count)
    b = N % (2 ** count)
    if a+1 <= K:
        print(2**(count) - b)
    count += 1
    print(count, a,b)
print(count, b)
print(2**(count-1) - b)