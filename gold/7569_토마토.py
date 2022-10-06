import sys
sys.setrecursionlimit(10**9)

def bfs(nodes):
    global N, M, H, count

    if not nodes:
        for i in range(H):
            for j in range(N):
                for h in range(M):
                    if graph_3[i][j][h] == 0:
                        count = 0
                        return
        return

    count += 1
    queue = []
    while nodes:
        h, i, j = nodes.pop()
        for dh, di, dj in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,-1),(0,0,1)):
            nh = h + dh
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and 0 <= nh < H and graph_3[nh][ni][nj] == 0:
                graph_3[nh][ni][nj] = 1
                queue.append((nh,ni,nj))
    bfs(queue)
    

M, N, H = map(int, sys.stdin.readline().split())
graph_3 = []
first_tomato = []
# 3차원 배열
for h in range(H):
    arr_1 = []
    for i in range(N):
        a = list(map(int, sys.stdin.readline().split()))
        arr_1.append(a)
        for j in range(M):
            if a[j] == 1:
                first_tomato.append((h,i,j))
    graph_3.append(arr_1)

count = 0
bfs(first_tomato)
print(count-1)

