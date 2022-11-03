'''
i = -M ~ M일 때를 전부 확인한다.
'''


def backtracking(i,j,word):
    global h, result
    if i < 0 or i >= N or j < 0 or j >= M or visited[i][j]:
        result.append(word)
        return
    else:
        backtracking(i)

N, M = map(int, input().split())
graph = []
for _ in range(N):
    arr = [int(i) for i in input()]
    graph.append(arr)

result = []
visited = [[0] * M for _ in range(N)]
for h in range(-min(N,M),min(N,M)+1):
    for i in range(N):
        for j in range(M):
            # 모든 범위의 수를 전부 구한다.
            #             
