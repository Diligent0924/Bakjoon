'''
heapq를 tuple 형태로도 사용할 수 있다. => 신기하군..
'''

import heapq
import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    value = int(sys.stdin.readline())
    if value == 0:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr)[1])
    else:
        heapq.heappush(arr, (abs(value), value))