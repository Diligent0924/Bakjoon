sero, garo = map(int, input().split())
graph = []
for _ in range(sero):
    graph.append(list(map(int, input())))

result = 1
for h in range(1,min(sero, garo)):
    for i in range(sero):
        for j in range(garo):
            if 0 <= i + h < sero and 0 <= j + h < garo: # 번위안에 있고
                if graph[i][j] == graph[i][j+h] == graph[i+h][j] == graph[i+h][j+h]: #같으면
                    result = max(result, (h+1)**2)

print(result)
