X = int(input())
arr = [64,32,16,8,4,2,1]

i = -1
count = 0
while True:
    i += 1
    if X - arr[i] >= 0:
        X -= arr[i]
        count += 1

    if X == 0:
        break

print(count)