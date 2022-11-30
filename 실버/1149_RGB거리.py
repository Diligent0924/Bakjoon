'''
색깔이 겹치면 안된다.
'''
# def backtracking(root, count):
#     global min_count
#     if count >= min_count: # 만약 현재 최소값보다 크다면 그냥 끝낸다.
#         return
#     if root == N-1:
#         min_count = count
#         return
#     else:
#         for i in range(3): # 0,1,2만 있으면 된다.
#             # if visited[root] != i:
#                 # visited[root+1] = i
#                 # backtracking(root+1, count + arr[root+1][i])
#                 # visited[root+1] = -1
#             if visited[-1] != i:
#                 visited.append(i)
#                 backtracking(root+1, count + arr[root+1][i])
#                 visited.pop()

# import sys
# input = sys.stdin.readline
# N = int(input()) # 집의 개수
# arr = {}
# for i in range(N):
#     arr[i] = list(map(int,input().split()))
# # arr = [list(map(int,input().split())) for _ in range(N)]
# min_count = 10000000
# # visited = [-1] * N
# visited = []
# for i in range(3):
#     # visited[0] = i
#     visited.append(i)
#     backtracking(0,arr[0][i])

# print(min_count)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
rgb = [arr[0]]
for i in range(1,N):
    rgb_list = [min(rgb[i-1][1],rgb[i-1][2])+arr[i][0], min(rgb[i-1][0],rgb[i-1][2]) + arr[i][1],min(rgb[i-1][0],rgb[i-1][1]) + arr[i][2]]
    rgb.append(rgb_list)
print(min(rgb[-1]))