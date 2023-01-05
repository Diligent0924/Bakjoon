# 앞으로 갔다가 뒤로 갔다가 둘다 가능해야 한다. => 이걸 몰랐네 ㄹㅇ
# 알고리즘을 풀 때 좀 더 생각을 많이 해야하며 여러가지 방법에 대해서 알 수 있어야겠다.
# 근데 왜 BFS로만 풀리는지는 아직까지 모르겠다. BFS로만 가장 빠르게 확인이 가능한 이유는 무엇일까?
def bfs():
    while queue:
        now = queue.pop()
        for i in range(now, N, arr[now]):
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[now] + 1
        
        for i in range(now,-1,-arr[now]):
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[now] + 1
    return visited[b]
                          
N = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())
a -= 1
b -= 1
visited = [-1] * N 
visited[a] = 0
queue = [a]
print(bfs())