N = int(input())
graph = [list(map(int ,input().split())) for _ in range(N)]
min_DP = [[0] * 3 for _ in range(N)] # min_DP값을 확인한다.
max_DP = [[0] * 3 for _ in range(N)] # max_DP값을 확인한다.

# 처음 시작값을 경우에 사용한다.
min_DP[0][0], min_DP[0][1], min_DP[0][2] = graph[0][0],graph[0][1],graph[0][2]
max_DP[0][0], max_DP[0][1], max_DP[0][2] = graph[0][0],graph[0][1],graph[0][2]

for i in range(1, N):
    min_DP[i][0] = graph[i][0] + min(min_DP[i-1][0], min_DP[i-1][1])
    min_DP[i][1] = graph[i][1] + min(min_DP[i-1][0], min_DP[i-1][1], min_DP[i-1][2])
    min_DP[i][2] = graph[i][2] + min(min_DP[i-1][1], min_DP[i-1][2])
    
    max_DP[i][0] = graph[i][0] + max(max_DP[i-1][0], max_DP[i-1][1])
    max_DP[i][1] = graph[i][1] + max(max_DP[i-1][0], max_DP[i-1][1], max_DP[i-1][2])
    max_DP[i][2] = graph[i][2] + max(max_DP[i-1][1], max_DP[i-1][2])

# print(min_DP)
# print(max_DP)
print(max(max_DP[N-1]), min(min_DP[N-1]))