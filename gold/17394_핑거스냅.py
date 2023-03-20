from collections import deque
N = int(input())

def isPrime(number):
    for m in range(2, int(number ** 0.5) + 1):
        if not number % m:     
            return False # 소수가 아니다.
    return True # 소수가 맞다.

def bfs(N,A,B):
    queue = deque([(0,N)])
    visited = set([N])
    while queue:
        # print(queue)
        value, node = queue.popleft()
        for i in (node//2, node//3, node+1, node-1):
            if A <= i <= B:
                if isPrime(i):
                    return value + 1
            if i not in visited and 0 < i <= 1000000:
                queue.append((value+1, i))
                visited.add(i)
    return -1
        
for _ in range(N):
    N, A, B = map(int, input().split())
    if A <= N <= B and isPrime(N):
        print(0)
    else:
        print(bfs(N,A,B))
    
    