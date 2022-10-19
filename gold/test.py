import heapq
a = [45, -653]
print(heapq.heapify(a))
heapq.heappush(a, 5)
print(a)
heapq.heappop(a)
print(a)