def bfs():
    


N = int(input())
M = int(input())

point = [[] for _ in range(N)]
for _ in range(N):
    a = list(map(int, input().split()))
    for i in range(len(a)):
        if a[i]:
            point[_].append(i)
            point[i].append(_)
plan = list(map(int, input().split()))          
print(point)
