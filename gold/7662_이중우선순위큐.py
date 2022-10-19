import heapq
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    max_arr = []
    for _ in range(N):
        a, b = input().split()
        if a == "I":
            b = int(b)
            heapq.heappush(arr, b)
            heapq.heappush(max_arr, (-b, b))
        else:
            if not arr:
                continue
            elif b == "1": # 최대값일 경우
                max_value = heapq.heappop(max_arr)[1]
                arr.remove(max_value)
            else: # 최대값 제거
                min_value = heapq.heappop(arr)
                max_arr.remove((-min_value, min_value))

    if not arr:
        print("EMPTY")
    else:
        # print(max(arr), min(arr))
        print(heapq.heappop(max_arr)[1], heapq.heappop(arr))