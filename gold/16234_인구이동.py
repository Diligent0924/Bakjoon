N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]

def dfs(i,j):
    global count, list_a, day

    already_a.append([i,j])
    list_a.append([i,j])
    count += arr[i][j]  
    print(count)
    if 0 <= i < N and 0 <= j < N:
        if L <= abs(arr[i][j] - arr[i][j+1]) <= R and [i,j+1] not in list_a:
            print(1)
            dfs(i,j+1)
        if L <= abs(arr[i][j] - arr[i][j-1]) <= R  and [i,j-1] not in list_a:
            dfs(i,j-1)
        if L <= abs(arr[i][j] - arr[i-1][j]) <= R  and [i-1,j] not in list_a:
            dfs(i-1,j)
        if L <= abs(arr[i][j] - arr[i+1][j]) <= R  and [i+1,j] not in list_a:
            print(2)
            dfs(i+1,j)
    else:
        return 

already_a = [] # 이미 들어가 있는 index
list_a = [] # 들어가있는 index
count_list = [] # count된 list
day = 0 # 처음날짜부터 얼만큼이나 돌아갔는가?
while True:
    day += 1
    for i in range(N):
        for j in range(N):
            count = 0
            dfs(i,j)
            print(count)
            print(list_a)
            print(f'already_a {already_a}')
            count_list.append(count)

            count = 0
            list_a = []
    already_a = []
    break