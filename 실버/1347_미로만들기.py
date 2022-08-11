# 오늘 교수님께서 알려주신 감마 길찾기 방법을 써봤다. => 매우 유용하다.

N = int(input())
arr = list(map(str, input()))
#전체 방을 생각해야한다.
graph = [[0] * 100 for _ in range(100)]
# 서남동북 순으로 생각하여 풀었다.
direction = [[0,-1],[1,0],[0,1],[-1,0]]
now_direction = 1
# 만약 R이면 현재 now_direction에서 하나 추가
a, b = 49, 49 # N이 최대 50이니까 밑으로만 꽂아도 100이 안넘기에 49를 해줬다.
graph[a][b] = "." # 처음에는 .으로 시작한다.
# R,L,F에 따라 각각이 다르게 지정했다.
for i in range(len(arr)): 
    if arr[i] == "R":
        now_direction -= 1
    elif arr[i] == "L":
        now_direction += 1
    elif arr[i] == "F":
        # 4로 나누어줘야 돌아간다.
        n,m = direction[now_direction%4]
        # 해당위치에 .을 찍어야한다.
        graph[a+n][b+m] = "."
        # 해당 위치로 변동해야하기 때문에 변동점을 두었다.
        a += n
        b += m

# 100 * 100 크기에서 .이 들어가는 크기만 잘라서 넣어야한다.
row_min, col_min, row_max, col_max = 101,101,0,0
for i in range(100):
    for j in range(100):
        if graph[i][j] == ".":
            row_min = min(row_min, i)
            row_max = max(row_max, i)
            col_min = min(col_min, j)
            col_max = max(col_max, j)
#print(row_min,row_max,col_min,col_max)

# result안에 필요한 구간만 잘라서 넣는다.
result = []
for i in range(row_min, row_max+1):
    list_a = []
    for j in range(col_min, col_max+1):
        if graph[i][j] == 0: # 구간을 잘랐으니 나머지 0은 #으로 변경해준다.
            graph[i][j] = "#"
        list_a.append(graph[i][j])
    result.append(list_a)

for i in result:
    for j in i:
        print(j, end="")
    print()