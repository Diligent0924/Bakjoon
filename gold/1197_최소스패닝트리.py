def find_set(x):
    while x != root[x]:
        x = root[x]
    return x


V, E = map(int, input().split())
root = [i for i in range(V+1)] # 기준치를 자기 자신으로 둔다.
database = []
for _ in range(E):
    u, v, w = map(int, input().split())
    database.append((w,u,v))

# 가중치가 짧은 순서대로 sort한다.
database.sort()

cnt = 0 # 모든 노드가 연결되면 자동으로 끝낸다.
weight = 0 # 가중치의 최소를 확인하기 위한 자료

# 짧은 순서대로 노드를 연결하되 대표 노드로 나타낸다.
for w, u, v in database: # u : 자기자신 / v : 가야되는 상대
    if find_set(u) != find_set(v): # 가장 대가리 부분만 연결하는 방식으로 선택
    # if find_set(u) != find_set(v): # 노드가 서로 연결되어 있지 않은 상태였다면
        cnt += 1
        weight += w
        root[find_set(v)] = find_set(u) # 이거 하나때문에 문제가 된다..?
        if cnt == V:
            break
        

print(weight)