'''
각각의 정사각형을 list형태로 둔다.

'''

W, H, f, c, x1, y1, x2, y2 = map(int, input().split())

# 현재 자기 자신의 index값을 확인
graph = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        graph[i][j] = [(i,j)]

# f로 접었을 때를 구한다.
for i in range(H):
    for j in range(f): # 가로로 f까지만!
        if j + f < W:
            graph[i][j+f].append((i,j))

# 세로로 동일한 구간으로 접을 때를 구한다.
visited = [[0] * W for _ in range(H)]
for i in range(1,H):
    if H // i == c+1:
        step = i
        break

break_count = 0
if not c:
    for i in range(0,H):
        for j in range(W%f,W):
            visited[i][j] = 1
else:
    for h in range(0,H,step):
        break_count += 1
        if break_count == c+1: # 만약 한번의 구간이 끝났다면 끝낸다?
            value = h
            break
        for i in range(h, h+step):
            for j in range(f,W):
                graph[i+step][j].extend(graph[i][j])
                if break_count == c:
                    print(f'real : {i},{j}')
                    visited[i+step][j] = 1

print(visited)
# x,y값으로 범위 구하기 => 해당 직사각형 크기 : H-1, f 를 (0,0)으로 잡고 시작
result = []
for n in range(abs(H-y2),abs(H-y1)):
    for m in range(abs(f+x1)%f,abs(f+x2)%f):
        print(n,m)
        if 0 <= n < H and 0 <= m < W and visited[n][m]:
            print(n,m)
            print(graph[n][m])
            result.extend(graph[n][m])

print(W*H - len(result))
for i in result:
    print(i)