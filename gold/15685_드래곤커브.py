'''
1. 선을 미리 저장한다. (선의 개수, 선의 방향)
2. 전체를 90도로 꺾을 때를 확인하여 반복한다.
3. 전체 point를 만든 후에 전체를 탐색하며 확인한다. (자기 기준으로 4방향을 확인)
'''
N = int(input())
arr = [[0] * 101 for _ in range(101)] # x,y 좌표를 100 X 100 형태로 나타낸다.
delta = (0,1),(-1,0),(0,-1),(1,0) # 순서대로 넣는다.

for _ in range(N):
    y,x,d,g = map(int, input().split())
    # print("--------------------")
    # 처음인 점을 넣는다.
    arr[x][y] = 1
    now_x, now_y = x, y
    # print(x,y)
    # 제일 처음일 때는 넣는다.
    a, b = x + delta[d%4][0], y + delta[d%4][1]
    if 0 <= a <= 100 and 0 <= b <= 100:
        now_x, now_y = a, b
        arr[a][b] = 1
    # print(now_x,now_y)
    if g == 0: # 만약 0이라면 한번만 하면 되기 때문에
        continue

    # 1번 커브
    count = 0
    stack = [d]
    while True:
        count += 1
        for i in stack[::-1]: # 뒤에서부터 역방향으로 이루어진다.
            direction = (i + 1) % 4 # 4로 나눈 나머지
            nx, ny = now_x + delta[direction][0], now_y + delta[direction][1]
            if 0 <= nx <= 100 and 0 <= ny <= 100:
                # print(nx,ny)
                arr[nx][ny] = 1
                now_x,now_y = nx, ny
                stack.append(direction)
        
        if count == g:
            break

result = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == arr[i+1][j] == arr[i+1][j+1] == arr[i][j+1] == 1:
            result += 1
print(result)