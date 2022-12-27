def dfs(root):
    if root == N:
    else:
        for i in range(N):
            visited[i] = 1
            dfs(root+1)
            visited[i] = 0
        
        
N = int(input())
graph = [list(int, input().split()) for _ in range(N)]
visited = [True] * N