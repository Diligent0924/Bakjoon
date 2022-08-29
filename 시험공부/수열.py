N = int(input())
arr = list(map(int, input().split()))

# 커지는 것을 먼저 확인
max_count = 0
count = 0
for i in range(N-1):
    if arr[i+1] >= arr[i]:
        count += 1
    else:
        max_count = max(count, max_count)
        count = 0

max_count = max(count, max_count)

count = 0
# 작아지는 것을 확인
for i in range(N-1):
    if arr[i+1] <= arr[i]:
        count += 1
    else:
        max_count = max(count, max_count)
        count = 0
max_count = max(count, max_count)

print(max_count+1)
