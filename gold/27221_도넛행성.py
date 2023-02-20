N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def circle(first, second, third,i,j): # 나머지 3개의 방향을 확인하는 경우
    circle_list = []
    for di, dj in (first, second, third):
        ni, nj = i + di, j + dj
        # print(ni,nj)
        if 0 <= ni < N and 0 <= nj < M and not graph[ni][nj]:
            graph[ni][nj] = 1
            circle_list.append((ni,nj))
    return circle_list

def other(o): # 하나만 따로 확인하는 경우
    ni, nj = o[0],o[1]
    other_list = []
    if not graph[ni][nj]:
        graph[ni][nj] = 1
        other_list.append((ni,nj))
    return other_list
 
def solution(start_i,start_j):
    # print("---------------------------")
    queue = [(start_i, start_j)]
    while queue:
        # print(queue)
        i, j = queue.pop()
        if j == M-1: # 오른쪽 끝
            circle_list = circle((1,0),(-1,0),(0,-1),i,j)
            queue.extend(circle_list)
            other_list = other((i,0))
            queue.extend(other_list)
        if j == 0: # 왼쪽 끝
            circle_list = circle((1,0),(-1,0),(0,1),i,j)
            queue.extend(circle_list)
            other_list = other((i,M-1))
            queue.extend(other_list)
        if i == N-1: # 아랫쪽
            circle_list = circle((-1,0),(0,-1),(0,1),i,j)
            queue.extend(circle_list)
            other_list = other((0,j))
            queue.extend(other_list)
        if i == 0: # 위쪽
            circle_list = circle((1,0),(0,-1),(0,1),i,j)
            queue.extend(circle_list)
            other_list = other((N-1,j))
            queue.extend(other_list)
        if i != 0 and i != N-1 and j != 0 and j != M-1:
            circle_list = circle((1,0),(-1,0),(0,-1),i,j)
            queue.extend(circle_list)
            other_list = other((i,j+1))
            queue.extend(other_list)

count = 0
for i in range(N):
    for j in range(M):
        if not graph[i][j]:
            count += 1
            graph[i][j] = 1
            # print(i,j)
            solution(i,j)
print(count)