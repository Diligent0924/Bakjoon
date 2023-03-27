'''
1. 2중 리스트를 생성한 후에 하나씩 밀어내는 방식을 사용한다. (2번째 pop(0) => 1번째 insert)
2. 벨트 안에 있는 로봇 리스트 생성 / 확인하며 이동
3. 올리는 위치에 로봇 하나 추가
4. 0의 개수를 확인하여 K개 이상일 때 종료
'''

N, K = map(int, input().split())
arr = list(map(int, input().split()))
container = [[0] * N for _ in range(2)]
for j in range(2):
    if j == 0:
        for h in range(N):
            container[j][h] = [arr.pop(0),0] # 내구도, 로봇
    if j == 1:
        for h in range(N-1,-1,-1):
            container[j][h] = [arr.pop(0),0]
print(container)
remain_robot = []
robot_index = 0
count = 0
while True:
    print(container)
    count += 1
    robot_index += 1 # 인덱스값을 하나씩 증가시키며 집어넣는다.
    result = 0
    for i in range(2): 
        for j in range(N):
            if container[i][j][0] == 0:
                result += 1
    if result >= K:
        break
    else:
        # 첫번째 끝을 아래로 내린다.
        a = container[0].pop()
        container[1].append(a)
        
        # 2번째의 처음을 1번째의 처음으로 올린다.
        b = container[1].pop(0)
        container[0].insert(0,b)
        
        # 컨테이너만 돌았을 경우에 로봇이 있다면 그냥 지운다.
        if container[0][N-1][1] != 0:
            remain_robot.remove(container[0][N-1][1])
            container[0][N-1][1] = 0
        
        # 로봇을 빠른 순서대로 한칸씩 옆으로 옮긴다.
        for j in range(N-2, -1, -1):
            if container[0][j][1]:
                if container[0][j+1][1] == 0 and container[0][j+1][0] >= 1:
                    container[0][j+1][1], container[0][j][1] = container[0][j][1], 0
                    container[0][j+1][0] -= 1
                        
        if container[0][N-1][1] != 0:
            # remain_robot.remove(container[0][N-1][1])
            container[0][N-1][1] = 0
        
        # 로봇을 올린다.
        if container[0][0][0] >= 1:
            container[0][0][0] -= 1
            container[0][0][1] = robot_index
            remain_robot.append(robot_index)
print(count-1)