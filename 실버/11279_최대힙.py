import heapq
import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    value = -(int(sys.stdin.readline()))
    if value == 0:
        if not arr:
            print(0)
        else:
            print(-(heapq.heappop(arr)))
    else:
        heapq.heappush(arr, value)
