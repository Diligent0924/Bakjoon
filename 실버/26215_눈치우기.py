'''
조금 해맨 부분
1. 매 반복마다 최댓값이 바뀐다는 것을 알고 넘어가야한다.
2. 
'''
import heapq
N = int(input())
arr = list(map(int, input().split()))
count = 0
while arr:
    heapq.heapify(arr)
    # print(arr)
    v = heapq.heappop(arr)
    count += v
    if len(arr):
        arr[-1] -= v
    # print(count)

# count = 0
# left, right = 0, len(arr)-1
# while left <= right:
#     arr.sort() # 반복적으로 sort시켜줘야한다?
#     if not arr[left]:
#         left += 1
#     elif not arr[right]:
#         right -= 1
#     elif right == left:
#         arr[left] -= 1
#         count += 1
#     else:
#         arr[left] -= 1
#         arr[right] -= 1
#         count += 1
if count > 1440:
    print(-1)
else:
    print(count)