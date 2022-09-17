'''
만약 N > M인 경우에는 *2가 의미가 없으므로 전체에서 빼야한다. ( 이 점을 간과했다. )
BFS는 생각보다 많은 곳에서 사용한다. => 어떤 반복적인 작업에도 사용할 수 있다는 것을 배웠다.
'''

def bfs(X, point):
    global result
    queue = []
    queue.append(X)
    while queue:
        node = queue.pop(0)
        if node == point:
            result = arr[node]
            return
        else:
            for d in (node-1, node+1, node*2):
                if 0 <= d < 100001 and arr[d] == 0:
                    arr[d] = arr[node] + 1
                    queue.append(d)





N, M = map(int, input().split())
arr = [0] * 100001
result = 0
bfs(N, M)
print(result)