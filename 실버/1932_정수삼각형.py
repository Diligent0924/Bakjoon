'''
제일 위에서부터 하나하나씩 확인하면서 백트래킹 하는 형태로 사용하면 될듯?
'''
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
def backtracking(root, index, count):
    global result
    if root == N:
        result = max(result, count)
        return
    else:
        if count + graph[root][index] > visited[root][index]:
            count += graph[root][index]
            visited[root][index] = count
            backtracking(root+1, index, count) # 오른쪽
            backtracking(root+1, index+1, count) # 왼쪽

N = int(input())
graph = []
visited = []
for i in range(N):
    arr = list(map(int,input().split()))
    visited.append([0] * (i+1))
    graph.append(arr)

result = 0
backtracking(0, 0, 0)
print(result)
