'''
최대깊이를 변경해줘야만 dfs로 풀이가 가능하다. => 안그럼 힘들듯!
델타알고리즘와 DFS의 차이
1. 델타알고리즘 => 해당 위치가 현재점으로 계속 변할 때 유용하게 사용
2. DFS => 특정 위치를 기준으로 퍼져나가는 형태에 사용
3. 델타알고리즘 + DFS => 전염병과 같이 어떤것이 지속적으로 퍼져나갈때 자주 사용
'''
import sys
sys.setrecursionlimit(10**6) # 깊이를 변화시켜준다.

def delta(i,j):
    global arr
    # 델타 알고리즘
    dx = [1,0,-1,0] 
    dy = [0,1,0,-1]
    if 0 <= i < sero and 0 <= j < garo: # 여기서 i는 높이 j는 길이를 나타낸다.
        if arr[i][j] == 0: # 만약 0이라면 재귀를 끝내야한다.
            return 0 # 보통 쓸게 없으면 0이라고 둔다!
        elif arr[i][j] == 1: # 만약 해당 값이 1이라면
            arr[i][j] = 0 # 0으로 바꿔준다.
            # 반복해서 사용한다. (계속 앞뒤양옆을 확인해야하므로..)
            delta(i+dx[0], j+dy[0])
            delta(i+dx[1], j+dy[1])
            delta(i+dx[2], j+dy[2])
            delta(i+dx[3], j+dy[3])
            return 0
    else:
        return 0
    

T = int(input())
for _ in range(T):
    garo,sero, bechu = map(int, input().split())
    arr = [[0] * (garo) for _ in range(sero)]
    # arr안에 있는 공간에 1을 넣기 (배추가 있는 곳)
    for _ in range(bechu):
        a, b = map(int, input().split())
        arr[b][a] = 1 # input이 가로 / 세로로 이루어져 있다.
    count = 0 # 지렁이의 개수를 센다.
    for i in range(sero):
        for j in range(garo):
            if arr[i][j] == 1:
                count += 1
                # 붙어있는 위치를 반복해서 사용한다.
                delta(i,j)
    print(count)