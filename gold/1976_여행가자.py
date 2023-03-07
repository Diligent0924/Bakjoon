'''
해당 문제의 경우 visited를 잘 사용할 수 있는가를 판단하는 문제이다.
나의 문제점
 - visited를 사용하지 않고 그냥 road에 있는 값을 하나하나씩 제거했기 때문에 최대 O(n) -> for문이 한번 더 쓰이는 문제 발생
 - 몇번을 거쳐도 상관이 없다 => 어떻게든 연결만 되어있다면 상관이 없다.
 - 문제에 대한 이해도가 부족함 => 알고리즘 문제를 풀기 전 한번 정도는 먼저 생각하고 문제를 풀어야한다.
 
해결방안
 - 이후 문제에서는 List에서 지우는 방식보다는 추가적인 기존의 List를 만들어 유지시키는 방향이 맞다고 생각됨
'''

def dfs(now):
    for pointer in point[now]:
        if not visited[pointer]:
            visited[pointer] = 1
            dfs(pointer)    


N = int(input())
M = int(input())

point = [set() for _ in range(N)]
for _ in range(N):
    a = list(map(int, input().split()))
    for i in range(len(a)):
        if a[i]:
            point[_].add(i)
            point[i].add(_)

plan = list(map(int, input().split()))
plan = [i-1 for i in plan]
visited = [0] * N
visited[plan[0]] = 1  
dfs(plan[0])

for i in plan:
    if not visited[i]:
        print("NO")
        exit()
print("YES")