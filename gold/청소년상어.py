# from pprint import pprint
from copy import deepcopy
def fish(a,arr):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == a: # 작은값부터 시작한다.
                # 물고기의 처음 방향 착하게 살거라 용찬아
                direction = arr[i][j][1] # 해당 위치부터 시작한다.
                # 물고기가 움직인다.
                d_count = 0
                while True:
                    d_count += 1
                    if d_count == 9: # 만약 8방향을 다 돌았다면 그냥 제자리에 둔다.
                        return
                    di, dj = delta[direction%8]
                    ni, nj = i + di, j + dj
                    if 0 <= ni < 4 and 0 <= nj < 4 and arr[ni][nj][0] != -1:
                        arr[i][j] = (a, direction)
                        arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j] # 위치 변경!
                        return # 한번만 변경하고 끝내야한다.
                    direction += 1


delta = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
def solution(s_i,s_j,s_d,count,graph): # i,j : 상어의 위치, s_d: 상어 방향, count:상어크기
    global result
    # 기존 물고기의 위치를 복사해서 붙여넣는다.
    arr = deepcopy(graph)
    # 물고기가 먼저 움직인다.
    for a in range(1,17):
        fish(a,arr)

    # pprint(arr)
    # print(s_i, s_j,s_d)
    # print(count)
    # 상어가 움직인다.
    for i in range(1,4):
        # print(s_d)
        di, dj = delta[s_d % 8][0] * i, delta[s_d % 8][1] * i
        ni, nj = s_i + di, s_j + dj
        # print(f'ni:{ni} nj{nj}')
        # print(f'di:{di} dj{dj}')
        if 0 <= ni < 4 and 0 <= nj < 4 and arr[ni][nj][0]: # 어떠한 물고기가 있어야만 갈 수 있다.
            arr_2 = deepcopy(arr)
            arr_2[s_i][s_j] = (0, 0)
            value = arr_2[ni][nj][0]
            arr_2[ni][nj] = (-1,arr_2[ni][nj][1]) # 상어가 먹은 자리는 -1, 현재 자리로 둔다.
            solution(ni,nj,arr_2[ni][nj][1], count+value, arr_2) # 상어가 먹고 다음 arr로 변경한다.
            result = max(result, count)
        else: # 만약 상어가 못간다면 값을 정의해줘야함
            result = max(result, count)



# 그래프를 차례대로 채워넣는다.
graph = [[0] * 4 for _ in range(4)]
for i in range(4):
    a,b,c,d,e,f,g,h = map(int, input().split())
    graph[i][0] = [a,b-1]
    graph[i][1] = [c,d-1]
    graph[i][2] = [e,f-1]
    graph[i][3] = [g,h-1]

f_count = graph[0][0][0]
graph[0][0][0] = -1

result = 0 # 해당 값
solution(0,0,graph[0][0][1],f_count,graph)
print(result)