import sys
N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr.append([a,b])

arr = sorted(arr, key=lambda x: (x[1],x[0]))

for i in arr:
    print(*i)