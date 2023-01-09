'''
heapq - 다익스트라는 처음 봤는데 엄청 빡세다.
그냥 다익스트라로 하는 것보다 heapq가 훤씬 빠르다는 것을 알 수 있었다.
왜 더 빠른 것인지에 대해서는 확인하기 어려웠다.

'''
import heapq
from sys import maxsize
import sys

inpput = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [maxsize] * (N+1) # maxsize에 대한 기능
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c,b)) # cost 기준으로 sort하기 위해서 
start, end = map(int, input().split())

def dijkstra(x):
    pq = []
    heapq.heappush(pq, (0, x)) # cost를 기준으로 줄어들어야하므로...
    visited[x] = 0 # 처음 start는 0으로 둬도 상관없음
    
    while pq:
        print(pq)
        d, x = heapq.heappop(pq) # d : cost, x : 시작값
        
        if visited[x] < d: # 만약 cost 값이 크면 다음으로 넘어간다.
            continue
        else:
            for nw, nx in graph[x]: # 전체를 확인하면서
                nd = d + nw # 기존 코스트를 더한다.

                if visited[nx] > nd:
                    heapq.heappush(pq, (nd, nx))
                    visited[nx] = nd
dijkstra(start)
print(visited[end])