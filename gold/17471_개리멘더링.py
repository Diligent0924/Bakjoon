'''
bfs ? dfs ? backtracking?
시간초과 엄청난다.. => 나중에 해보자! 고쳐야함!!
'''
def subset(arr): # 만약 길이 여러 곳으로 갈 수 있다면 전부 가봐야함.
    sub = []
    T = len(arr)
    for i in range(1<<T):
        temp = []
        for j in range(T):
            if i & (1<<j):
                temp.append(arr[j])
        if temp:
            sub.append(temp)
    return sub

def rev(): # 나머지 0인 얘들끼리 묶여있는지 확인하기
    for i in range(1,N+1):
        if not visited[i]:
            queue = [i]
            while queue:
                node = queue.pop()
                if not visited[node]:
                    visited[node] = 2
                    queue.extend(link[node])
            break
    # 다 돌았으면 visited에 0이 없는지를 확인
    for i in range(1,N+1):
        if not visited[i]:
            return False
        elif visited[i] == 2: # 2는 다시 0으로 바꿔줘야한다.
            visited[i] = 0 
    return True # 중간에 0이 없었다면 끝낸다.

def bfs(start,count):
    global result
    # print(start,count)
    # 반대쪽이 전부 연결되어 있는지를 확인하기
    opposite = rev()
    if opposite:
        # print(sum(arr), count)
        result = min(result, abs(sum(arr)-1-count-count))
        # print(f'result : {result}')

    # 아직 방문하지 않는 노드들을 구한다.
    nodes = []
    for k in start:
        for node in link[k]:
            if not visited[node]:
                nodes.append(node)

    # print(f'nodes:{nodes}')
    if not nodes: # 만약 더 이상 갈 수 있는 곳이 없다면 끝낸다.
        return
    else: # 1개 이상이면 전체를 뽑아서 간다.
        sub = subset(nodes)
        # print(f'sub: {sub}')
        for data in sub:
            for m in data:
                visited[m] = 1
                count += arr[m]
            bfs(data, count)
            for m in data:
                visited[m] = 0
                count -= arr[m]





N = int(input())
arr = [1] + list(map(int, input().split()))
link = [1]
for _ in range(N):
    a = list(map(int, input().split()))
    a.pop(0)
    if not a:
        link.append([])
    else:
        link.append(a)

# print(arr)
# print(link)
result = 1000000
for i in range(1,N+1): # 모든 구역에서 들어가본다.
    visited = [1] + [0] * N
    visited[i] = 1 # 시작한 곳은 방문한 곳이다.
    # print('------------')
    bfs([i],arr[i])
    visited[i] = 0

if result == 1000000:
    print(-1)
else:
    print(result)