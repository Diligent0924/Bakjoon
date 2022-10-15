'''
시간과 연관된 부분에 있어서는 while문을 2번 돌리는 방식으로 사용해야하며 그 안의 조건들을 걸어가면서 푸는 방식
'''

def solution(): # 처음에 어디에 값이 있는지를 확인하는 함수
    q = []
    for number in range(1, K+1):
        for i in range(N):
            for j in range(N):
                if graph[i][j] == number:
                    q.append((i,j,number))
    return q            

def bfs(queue): 
    temp_queue = [] # 임시함수로써 이후에 time과 연관되게 하기 위한 하나의 방식
    while queue:
        i,j, number = queue.pop(0)
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and not graph[ni][nj]:
                graph[ni][nj] = number
                temp_queue.append((ni,nj,number))
    return temp_queue
                            
    


N, K = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
time, result_i, result_j = map(int, input().split())
now = 0
if now == time: # 만약 0초라면 그냥 바로 확인해본다.
    print(graph[result_i-1][result_j-1]) 
else: # 0초가 아니라면 시간이 가게끔 만든다.
    first = solution() # 초기에 필요한 값을 구한다.
    queue = []
    queue.extend(first) # 처음에 들어가는 값을 queue에 저장
    while True:
        # print(queue)
        now += 1
        queue = bfs(queue) # queue가 다 돌면 다시 새로운 것을 할당한다.
        # print(graph)
        if now == time:
            print(graph[result_i-1][result_j-1])
            break