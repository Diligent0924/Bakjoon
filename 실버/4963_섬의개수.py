import sys
sys.setrecursionlimit(10**6)

def bfs(y,x):
    if y < 0 or y >= h or x < 0 or x >= garo or graph[y][x] == 0:
        return
    else:
        graph[y][x] = 0
        bfs(y, x+1)
        bfs(y, x-1)
        bfs(y+1, x)
        bfs(y-1, x)
        bfs(y+1, x+1)
        bfs(y+1, x-1)
        bfs(y-1, x+1)
        bfs(y-1, x-1)


count_list = []
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    garo = len(graph[0])
    count = 0 
    for i in range(h):
        for j in range(garo):
            if graph[i][j] == 1:
                count += 1
            bfs(i,j)
    count_list.append(count)

for i in count_list:
    print(i)