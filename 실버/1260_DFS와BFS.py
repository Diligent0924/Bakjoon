'''
정점의 개수 : N / 간선의 개수 : M / 탐색 시작번호 : V
양방향이다. 문제 2번 읽고 풀기! 시간은 남는다.
'''
def dfs(arr, S):
    stack,visited = [S], []
    while stack:
        # print(f'stack : {stack} visited:{visited}')
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(arr[node])
    return visited

def bfs(arr, S):
    queue = [S]
    visited = []
    while queue:
        # print(f'queue : {queue} visited:{visited}')
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(arr[node])
    return visited

N, M, V = map(int,input().split())
arr = [[] for _ in range(N)]
arr_2 = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int,input().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)
    arr_2[a-1].append(b-1)
    arr_2[b-1].append(a-1)

for i in range(N):
    arr_2[i] = sorted(arr[i], reverse=True)

for i in range(N): # 한번더 sorted 해줘야한다.
    arr[i] = sorted(arr[i])


print(*list(map(lambda x: x+1, dfs(arr_2, V-1))))
print(*list(map(lambda x: x+1, bfs(arr, V-1))))