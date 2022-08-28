'''
위로 한칸씩 올라가는 방법이 더 빠르다. => 문제를 풀 때 고민해서 풀면 될 것 같다.
'''

N = int(input())
arr = [0] * 1001
for _ in range(N):
    a, b = map(int, input().split())
    arr[a] = b

max_height = max(arr)
left = 0
right = 1000
count = 0

for i in range(1, max_height+1):
    left, right = 0, 0
    for j in range(1001):
        if arr[j] >= i:
            left = j
            break
    for j in range(1000, -1, -1):
        if arr[j] >= i:
            right = j
            break

    count += right - left

count += max_height
print(count)