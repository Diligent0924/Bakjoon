'''
2개로 나눌 수 있는 모든 경우의 수를 구한다. => 가능한 모든 경우의 수를 구한 후에 반으로 나누면 되지 않을까?
값을 구한다.
'''
def solution(root):
    global visited, N, team, temp
    if root == N:
        temp_1 = temp[:N//2]
        temp_2 = temp[N//2:]
        temp_1.sort()
        temp_2.sort()
        if (temp_1, temp_2) not in team and (temp_2, temp_1) not in team:
            team.append((temp_1, temp_2))
        return
    else:
        for i in range(0, N):
            if visited[i]:
                continue
            else:
                visited[i] = 1
                temp[root] = i
                solution(root+1)
                visited[i] = 0
    
# 2개를 확인하는 함수
def a_score(root):
    global a_count, a_visited, a_temp
    if root == 2:
        # print(f"a_temp :{a_temp}")
        f, s = a_temp
        a_count += graph[f][s]
        return
    else:
        for i in range(len(a)):
            if a_visited[i]:
                continue
            else:
                a_visited[i] = 1
                a_temp[root] = a[i]
                a_score(root+1)
                a_visited[i] = 0

def b_score(root):
    global b_count, b_visited, b_temp
    if root == 2:
        # print(f"b_temp : {b_temp}")
        f, s = b_temp
        b_count += graph[f][s]
        return
    else:
        for i in range(len(b)):
            if b_visited[i]:
                continue
            else:
                b_visited[i] = 1
                b_temp[root] = b[i]
                b_score(root+1)
                b_visited[i] = 0
                
                
        
        
        
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
result = 100000000

team = []
visited = [0] * (N+1)
temp = [0] * N
solution(0)

for a, b in team:
    # a_team 먼저 확인
    a_visited = [0] * N
    a_temp = [-1] * 2
    a_count = 0
    a_score(0)
    # b_team 확인
    b_visited = [0] * N
    b_temp = [-1] * 2
    b_count = 0
    b_score(0)
    
    result = min(result, abs(a_count - b_count))

print(result)