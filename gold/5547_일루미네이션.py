'''
정육각형을 어떻게 판별할 것인가에 대한 문제
정육각형 문제
1. 층별로 다를 수밖에 없으므로 행에 따라서 다르게 나타내야 한다.
2. 중간의 빈 공간을 먼저 확인하고 그 이후에 채운 공간을 다시 확인한다.
3. 로직 처리를 좀 더 생각해보고 문제를 그 후에 푸는 습관을 들여야겠다.
4. 서순 문제가 매우 많았다. 예) 전체를 확인한 후에 지워야하나 중간에 return 값을 주는 등의 행위

=> 해당 문제가 실제로 나왔다면 풀기 어려웠을 것이다. 좀 더 확실하게 생각하면서 문제를 풀어야 한다.

'''
from copy import deepcopy
from pprint import pprint
def is_nth(i):
    if not i % 2:
        return nth
    else:
        return notnth
    
def in_box(start_i,start_j):
    global result
    in_box_number = 0
    queue = [(start_i,start_j)]
    in_box_graph[start_i][start_j] = 1 # 1로 변환해서 판단
    in_box_visited[start_i][start_j] = 1 # visited로 판단
    zero = False
    while queue:
        i, j = queue.pop(0)
        number = 6
        delta = is_nth(i)
        for di, dj in delta:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if not in_box_graph[ni][nj]:
                    in_box_graph[ni][nj] = 1
                    in_box_visited[ni][nj] = 1
                    queue.append((ni,nj))
                    number -= 1
                elif in_box_graph[ni][nj] == 1 and in_box_visited[ni][nj]:
                    number -= 1
            elif ni < 0 or ni >= N or nj < 0 or nj >= M: # 하나라도 바깥쪽과 연결되어 있다면 끝낸다.
                zero = True
        # pprint(in_box_graph)
        # print(i,j, number)
        in_box_number += number
    
    if zero:
        return 0
    else:
        return in_box_number
    
    
def bfs(start_i,start_j):
    global result
    queue = [(start_i,start_j)]
    graph[start_i][start_j] = 0 # 시작하는 점을 0으로 변환
    visited[start_i][start_j] = 1 # 방문한 곳으로 판단
    while queue:
        i, j = queue.pop(0)
        number = 6 # 6개부터 시작하므로
        delta = is_nth(i)
        for di, dj in delta:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if graph[ni][nj]:
                    graph[ni][nj] = 0
                    visited[ni][nj] = 1
                    queue.append((ni,nj))
                    number -= 1 # 하나씩 빼준다.
                elif visited[ni][nj]:
                    number -= 1
        result += number
        
                    
                

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
in_box_graph = deepcopy(graph)
notnth = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(0,1)]
nth = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(0,-1)]
visited = [[0] * M for _ in range(N)]
in_box_visited = [[0] * M for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if not in_box_graph[i][j]:
            # print(f'i : {i}, j : {j}')
            num = in_box(i,j)
            # print(f'num : {num}')
            result -= num

for i in range(N):
    for j in range(M):
        if graph[i][j]:
            bfs(i,j)
            # print(result)
print(result)