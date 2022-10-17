'''
처음 : 만약 거리가 20 * 50 이면 끝낸다.
아니라면 : 근처 가게로 간다.
'''
from collections import deque
import sys
input = sys.stdin.readline
def bfs():
    global result
    queue = deque([(s_i,s_j)])
    while queue:
        i, j = queue.popleft()
        if abs(e_j - j) + abs(e_i - i) <= 1000:
            result = 1
            return 
        for h in range(N):
            if not visited[h]:
                ni, nj = store[h]
                if abs(ni-i) + abs(nj-j) <= 1000:
                    visited[h] = 1
                    queue.append((ni,nj))

# def dfs(i, j):
#     global result, e_i, e_j, break_i
#     if break_i:
#         return
#     if abs(e_j - j) + abs(e_i - i) <= 1000:
#         result = 1
#         break_i = True
#         return
#     else:
#         for h in range(N):
#             if visited[h]:
#                 continue
#             else:
#                 ni, nj = store[h]
#                 if abs(ni-i) + abs(nj-j) <= 1000:
#                     visited[h] = 1
#                     dfs(ni, nj)
#                     visited[h] = 0
        

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    s_i, s_j = map(int, input().split())
    store = []
    visited = [0] * N
    for _ in range(N):
        store.append(list(map(int, input().split())))
    e_i, e_j = map(int, input().split())
    
    # 거리를 잰다.
    result = 0
    # break_i = False
    # dfs(s_i, s_j)
    bfs()
    if result:
        print('happy')
    else:
        print('sad')