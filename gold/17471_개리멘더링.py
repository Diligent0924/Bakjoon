'''
subset으로 하나하나씩 확인한 후에 다가가는 방식이다.
특이한 케이스 존재 => 어떤 구간에 1개만 들어가고 아무와도 연관이 없더라도 하나의 구역으로 쳐야한다.
굉장히 어려운 문제였음
처음 문제를 풀 때 팀1, 팀2일때의 모든 경우의 수를 구하는 방식으로 나아가는 것이 좀 더 편함
문제풀이 : 팀을 2개로 모든 경우로 나눈 후 => 최적값을 오름차순으로 소팅함(작은것부터 시작해서 조건에 맞으면 바로 끝냄)
조건풀이 : 서로 팀의 노드들이 연결되어 있는지를 확인한다. => 이 때 1개만 들어있는 경우에도 구간을 1개라고 쳐야한다.
'''
def subset(arr):
    T = len(arr)
    for i in range(1<<T):
        team_1, team_2 = [], []
        team_1_count, team_2_count = 0, 0 
        for j in range(T):
            if i & (1<<j):
                team_1.append(arr[j])
                team_1_count += population[arr[j]]
        # 팀 1이 아닌 나머지 구간
        for h in range(1,N+1):
            if h not in team_1:
                team_2.append(h)
                team_2_count += population[h]
        teams.append((team_1,team_2,abs(team_1_count-team_2_count)))
    
N = int(input())
population = [0] + list(map(int,input().split()))
nodes = [[]]
for _ in range(N):
    a = list(map(int,input().split()))
    b = a.pop(0)
    nodes.append(a)


teams = []
subset([i for i in range(1,N+1)])
teams.sort(key=lambda x: x[2]) # 크기가 작은 순서대로 sorting 후에 찾으면 편하다!
# print(teams)
for team_1, team_2, result in teams:
    # print(team_1,team_2, result)
    # 연결이 제대로 되어있는지 확인하는 작업이 필요하다.
    final_stack_1 = []
    if len(team_1) == 1: # 하나만 들어있는 경우에도 구간을 하나라고 판단한다.
        pass
    else:
        if team_1:
            visited_1 = [0] * (N+1)
            stack_1 = []
            stack_1.append(team_1[0])
            while stack_1:
                node = stack_1.pop()
                for h in nodes[node]:
                    if not visited_1[h] and h in team_1:
                        visited_1[h] = 1
                        stack_1.append(h)
                        final_stack_1.append(h)
        # print(f'final_stack_1:{final_stack_1}')
        final_stack_1.sort()
        if final_stack_1 != team_1: #만약 안된다면 다음 방법으로 넘어간다.
            continue

    if len(team_2) == 1: # 하나의 지역만 있더라도 구간을 하나라고 판단해야한다. => 특이케이스(매우 조심해야함.)
        print(result)
        quit()
    visited_2 = [0] * (N+1)
    final_stack_2 = []
    stack_2 = []
    stack_2.append(team_2[0])
    # print(stack_2)
    while stack_2:
        node = stack_2.pop()
        for h in nodes[node]:
            if not visited_2[h] and h in team_2:
                visited_2[h] = 1
                stack_2.append(h)
                final_stack_2.append(h)
    final_stack_2.sort()
    # print(f'final_stack_2:{final_stack_2}')      
    if final_stack_2 == team_2: #만약 안된다면 다음 방법으로 넘어간다.
        print(result)
        quit()
print(-1)