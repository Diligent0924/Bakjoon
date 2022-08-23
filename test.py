import sys
sys.setrecursionlimit(10**4) # 깊이를 변화시켜준다.

from copy import deepcopy
def dfs(i,j):
    global count, visited,count_count_dic
    visited[i][j] = arr_count
    if visited[i][j] not in count_count_dic:
        count_count_dic[visited[i][j]] = 1
    else:
        count_count_dic[visited[i][j]] += 1
    count += arr[i][j]
    if 0 <= i <= N-1 and 0 <= j <= N-1:
        if j+1 < N:
            if L <= abs(arr[i][j] - arr[i][j+1]) <= R and visited[i][j+1] == 0: # 뒤에부분...
                dfs(i,j+1)
        if j-1 >= 0:
            if L <= abs(arr[i][j] - arr[i][j-1]) <= R  and visited[i][j-1] == 0:
                dfs(i,j-1)
        if i-1 >= 0:
            if L <= abs(arr[i][j] - arr[i-1][j]) <= R  and visited[i-1][j] == 0:
                dfs(i-1,j)
        if i+1 < N:
            if L <= abs(arr[i][j] - arr[i+1][j]) <= R  and visited[i+1][j] == 0:
                dfs(i+1,j)
    else:
        return 

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]

day = 0 # 처음날짜부터 얼만큼이나 돌아갔는가?
while True:
    a = deepcopy(arr)
    count_count_dic = {}
    count_list = {}
    day += 1
    visited = [[0] * N for _ in range(N)] # 방문했는지 안했는지를 확인하는 방법
    arr_count = 0
    count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] != 0:
                continue
            else:
                # 해당되는 영역을 구분하기 위하여 사용
                arr_count += 1
                count = 0 # 해당 영역에서의 합을 구한다.
                dfs(i,j)
                count_list[arr_count] = count # 해당 영역과 영역의 합을 구한다.
    print(visited)
    print(arr)
    
    # 해당되는 구분에 따라서 arr를 변경하기 위해서 사용한다.
    for i in range(N):
        for j in range(N):
            if visited[i][j] in count_list:
                arr[i][j] = count_list[visited[i][j]] // count_count_dic[visited[i][j]]
    #print(arr)
    
    
    if a != arr:
        continue
    else:
        print(day-1)
        break