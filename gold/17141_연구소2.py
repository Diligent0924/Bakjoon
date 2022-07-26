'''
순열과 조합에 대해서 정확하게 알  필요가 있다.
순열 : 순서가 상관있는것
조합 : 순서가 상관없는것
=> 이 문제는 조합으로 문제를 풀어야함 : 조합문제풀이 => subset구하기 >>
'''
# 바이러스가 M개가 될 때의 경우의 수를 구한다.
from random import vonmisesvariate


def subset():
    for i in range(1<<len(virus_spot)):
        temp = []
        for j in range(len(virus_spot)):
            if i & (1<<j):
                temp.append(virus_spot[j])
                if len(temp) > M:
                    break
        if len(temp) == M: # 개수가 M개인 List의 조합을 구하는 방법임
            # print(temp)
            for a, b in temp:
                graph[a][b] = 5
            bfs(temp, 0)
            for i in range(N):
                for j in range(N):
                    if graph[i][j] == 4:
                        graph[i][j] = 0
                    elif graph[i][j] == 5:
                        graph[i][j] = 2

def bfs(queue, time):
    # print(f'queue : {queue}')
    global result
    if time >= result: # 만약 시간이 result보다 큰 경우에는 더 돌릴 필요가 없으므로 끝낸다.
        return

    temp = []
    while queue:
        i,j = queue.pop()
        for di, dj in ((0,1),(0,-1),(1,0),(-1,0)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if not graph[ni][nj]:
                    graph[ni][nj] = 4
                    temp.append((ni,nj))
                elif graph[ni][nj] == 2:
                    graph[ni][nj] = 5
                    temp.append((ni,nj))

    # queue가 한번 다 돌고 나서 확인한다.
    for i in range(N):
        for j in range(N):
            if not graph[i][j] or graph[i][j] == 2: # 0이나 2 두개를 모두 지워야한다.
                if not temp: # 0인데 temp 또한 없다면 못가는 경우가 있으므로 끝!
                    return
                else:
                    bfs(temp, time+1) 
                    return # 1번만 돌고 끝내게 한다.
    # 전체가 꽉 차게 된다면 끝낸다.
    result = time+1
    return




N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 바이러스가 퍼질 수 있는 곳을 찾는다.
virus_spot = []
zero_count = 0 
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus_spot.append((i,j))
        elif not graph[i][j]:
            zero_count += 1

# 모든 바이러스가 기존에 있을 수 있다는 예외처리가 필요하다! (이런 디버깅 실력... 필요하다!)
if len(virus_spot) == M and not zero_count:
    print(0)
else: 
    result = 1000000 # 시간을 준다.
    subset()
    if result == 1000000:
        print(-1)
    else:
        print(result)