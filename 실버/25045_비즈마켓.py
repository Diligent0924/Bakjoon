N, M = map(int, input().split())
stock = sorted(list(map(int, input().split())), reverse=True)
business = sorted(list(map(int, input().split())))

count = 0
for a,b in zip(stock, business):
    if b - a > 0:
        continue
    else:
        count += a-b

print(count)