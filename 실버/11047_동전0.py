N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
count = 0
for i in range(N-1, -1, -1):
    if K >= arr[i]:
        count += K // arr[i]
        K = K % arr[i]

print(count)