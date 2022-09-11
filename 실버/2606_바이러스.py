'''
BFS로 문제를 푸는 방식이다. => 그래프 완전탐색
아직 양방향일 때와 단방향일 때의 차이점을 잘 모르겠다. => BFS에서 양방향과 단방향의 차이는 무엇인가?
'''
def bfs(S):
    queue = [S]
    visited = [0] * (N+1)
    while queue:
        node = queue.pop(0)
        if visited[node] == 0:
            queue.extend(arr[node])
            visited[node] = 1
    return visited

N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

print(sum(bfs(1)) - 1)