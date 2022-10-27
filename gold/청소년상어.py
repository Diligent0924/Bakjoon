'''
청소년 상어 시작 : (0,0)
물고기는 크기가 작은 얘부터 시작해서 큰 얘가 계속 움직이는 방식으로 하고 마자막은 청소년 상어가 움직임
상어가 갈 수 있는 모든 방법의 수를 Backtracking해서 움직어야할거 같다.
상어 이전 물고기들의 위치를 돌려놔야하는데 어떻게 해야 돌려놓을 수 있을까?
'''

def find(h):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == h:
                fish(i,j,arr[i][j][1],1)
                return

def fish(i,j,direction, n):
    di, dj = delta[(direction-1) % 8]
    ni, nj = i + di, j + dj
    # 상어 위치가 아니고 범위 안에 들어간다면 자리를 옮긴다. (방향은 돌려진 상태의 방향을 그대로 가져간다.)
    if 0 <= ni < 4 and 0 <= nj < 4 and arr[ni][nj][0] != -1:
        arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]
        arr[ni][nj][1] = direction # 해당 direction을 그대로 가지고 있는게 맞다.
        return 
    else:
        if n == 8: # 만약 8방향을 전부 가봤다면 끝낸다.(위치 그대로)
            return 
        else: # 아니라면 45도 방향으로 다시 나가본다.
            fish(i,j, direction+1, n+1)

def shark(i,j,direction, time, count):
    global result, time_fish, fish_value, arr
    print(f"previous : {arr}")
    if time > 17:
        return

    # 현재 물고기의 위치를 파악하여 저장한다.
    time_fish.append(arr)
    print(f'timefish:{time_fish}')
    # 물고기의 위치를 변화시킨다.
    for h in range(1,17):
        find(h)

    dx = delta[(direction-1) % 8]
    for k in range(1,4): # 상어가 이동해서 먹을 수 있는 방법
        di, dj = dx[0] * k, dx[1] * k
        ni, nj = i + di, j + dj
        if 0 <= ni < 4 and 0 <= nj < 4 and not visited[ni][nj]:
            visited[ni][nj] = 1
            v = arr[ni][nj][0]
            fish_value.append(arr[ni][nj][0])
            arr[ni][nj][0] = -1
            shark(ni,nj,arr[ni][nj][1],time+1,count+v)
            arr[ni][nj][0] = fish_value.pop() # 마지막 값에서 빠진다.
            print(f'arr : {arr[ni][nj][0]}')
            visited[ni][nj] = 0
    
    # 물고기의 위치를 원래대로 돌린다.
    arr = time_fish.pop()
    print(f'return : {arr}')
    # print(f'time : {time} count : {count}')
    print(arr)
    print(count)
    result = max(result, count)
    return # for문에서 빠져나왔다면 더이상 갈곳이 없는 것이므로 끝낸다.


delta = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)] # 왼쪽방향부터 45도 방향(반시계)
# 4*4인 값을 넣어놓는다.
arr = [[0] * 4 for _ in range(4)]
result = 0 
for i in range(4):
    a,b,c,d,e,f,g,h = map(int,input().split())
    if not i:
        arr[i][0] = [-1,b]
        start = a
    else:
        arr[i][0] = [a,b]
    arr[i][1] = [c,d]
    arr[i][2] = [e,f]
    arr[i][3] = [g,h]



# 물고기들이 전부 다 돌아다녔다면 상어가 움직인다. => 상어는 상어의 해당 방향으로 움직이며 어디든 갈 수 있다.
time_fish = [] # 물고기들의 위치 저장
fish_value = [] # 상어한테 먹힌 물고기 되돌리기 위한 리스트
visited = [[0] * 4 for _ in range(4)]
visited[0][0] = 1
shark(0,0,arr[0][0][1],1,start) # 0,0,방향,시간, 개수
print(result)