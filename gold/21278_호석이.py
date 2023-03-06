'''
호석이 두마리 치킨 => 도시 내 2개의 매장
'''
from itertools import combinations
from collections import deque
import sys
def road(now): # BFS 형태로 저장
    visited = [0] * N
    queue = deque([(now,0)])
    while queue:
        n, n_count = queue.popleft()
        if not visited[n]:
            visited[n] = n_count + 1
            for h in point[n]:
                queue.append((h, n_count+1))
    return visited

input = sys.stdin.readline
N, M = map(int, input().split()) # 건물의 수 / 도로의 수
L = [i for i in range(N)]
point = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    point[a-1].append(b-1) # 양방향 더하기
    point[b-1].append(a-1)

combination_list = list(combinations(L, 2)) # 전체의 개수를 정한다.
# print(point)
min_a = -1
min_b = -1
min_count = 10000000000
for a, b in combination_list: # 치킨집의 위치 확인
    # print(a,b)
    count = 0
    # 치킨집 A와 B에서 가는 경우를 판단한다.
    visited_a = road(a)
    visited_b = road(b)
    count = 0
    # print(visited_a, visited_b)
    for va, vb in zip(visited_a, visited_b):
        count += min(va-1, vb-1) * 2

    if count < min_count:
        min_a = a + 1
        min_b = b + 1
        min_count = count

print(min_a, min_b, min_count)        