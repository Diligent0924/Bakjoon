from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 치킨집 위치를 먼저 구한다.
chickenzip = []
house = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chickenzip.append((i,j))
        if graph[i][j] == 1:
            house.append((i,j))

# 치킨집이 M개인 경우의 수를 모두 구한다.
list_a = [1,2,3,4]
a = list(combinations(chickenzip,M))

# 경우의 수에 따른 치킨 집을 구한다.
result = 10000000000
for chicken_houses in a:
    little_distace = 0
    for house_i, house_j in house: # 각각의 집에서 출발한다.
        value = 100000000
        for chicken_i, chicken_j in chicken_houses:
            value = min(value, abs(house_i - chicken_i) + abs(house_j - chicken_j))
        little_distace += value

    result = min(result, little_distace) # 더 작은 값을 결론으로 낸다.
print(result)