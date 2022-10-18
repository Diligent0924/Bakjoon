'''
현재 방향의 왼쪽 방향으로 확인한다.
-1, -2, -3을하면 되지않을까? => 어차피 방향이 왼쪽이니까~
'''
def direction_change(now):
    if now == "north":
        return "west"
    elif now == "west":
        return "south"
    elif now == "south":
        return "east"
    elif now == "east":
        return "north"

def machine(i,j,d):
    graph[i][j] = 2 # 해당 부분은 청소를 했다.
    count = 0
    while True:
        count += 1 
        if count == 5: # 만약 방향을 5번 돌았다면 (4방향에서 안된다면)
            di, dj = d
            di, dj = -di, -dj # 뒤로가는 것을 계산한다.
            ni, nj = i + di, j + dj
            if graph[ni][nj]:
                return
            else:
                machine(i+di,j+dj,d) # 뒤로 한칸씩 들어간다.
        else:
            now_d = direction_change(d)
            d = now_d
            di, dj = now_d
            ni = i + di
            nj = j + dj
            if 0 <= ni < sero and 0 <= nj < garo:
                if graph[ni][nj] == 0: # 만약 있다면 해당 부분 재귀 + 끝낸다.
                    machine(ni,nj,d)
                    return
                elif 

Dic = {"north":(-1,0), "west":(0,1), "south":(1,0), "east":(0,-1)}
sero, garo = map(int,input().split())
i, j, d = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(sero)]
