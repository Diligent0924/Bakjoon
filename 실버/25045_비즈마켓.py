N, M = map(int, input().split())
stock = list(map(int, input().split()))
business = list(map(int, input().split()))

stock.sort(reverse=True)
business.sort()

count = 0
for a,b in zip(stock, business):
    if b - a > 0:
        continue
    else:
        count += a-b

print(count)