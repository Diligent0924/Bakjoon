'''
물을 먼저 확인 => 고슴도치 움직일 수 있는 공간 확인 순서로 한다.

'''
def solution(gosem, water,count):
    global result, gosem_visited
    temp_gosem = []
    temp_water = []
    # 물이 먼저 확산될 수 있도록 한다.
    while water:
        water_i, water_j = water.pop()
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni = water_i + di
            nj = water_j + dj
            if 0 <= ni < R and 0 <= nj < C and graph[ni][nj] == '.':
                temp_water.append((ni,nj))
                graph[ni][nj] = '*'

    # 고슴도치가 움직인다. => 고슴도치가 움직이는 것은 graph상에 따로 표시할 필요는 없다.
    while gosem:
        gosem_i, gosem_j = gosem.pop()
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni = gosem_i + di
            nj = gosem_j + dj
            # 도착지에 왔다면 result와 비교하고 끝낸다.

            if 0 <= ni < R and 0 <= nj < C:
                if graph[ni][nj] == "D":
                    result = min(result, count)
                    break
                elif graph[ni][nj] == '.' and (ni,nj) not in gosem_visited:
                    gosem_visited.append((ni,nj))
                    temp_gosem.append((ni,nj))
                    
    if not temp_water and not temp_gosem:
        return
    else:
        solution(temp_gosem, temp_water, count+1)

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
gosem_list = []
water_list = []
for i in range(R):
    for j in range(C):
        if graph[i][j] == "S":
            gosem_list.append((i,j))
        elif graph[i][j] == "*":
            water_list.append((i,j))

gosem_visited = []
result = 10000000
solution(gosem_list, water_list, 1)
if result == 10000000:
    print("KAKTUS")
else:
    print(result)
