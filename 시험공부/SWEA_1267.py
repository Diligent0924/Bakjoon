'''
1. 아무영향도 받지않는 첫번쨰
'''
def solution(node,visited):
    for i in range(len(arr)):
        # print(arr[i])
        if node in arr[i] and arr.index(arr[i]) not in visited:
            return False
    return True

def bfs():
    queue = []
    visited = []
    queue.append(start_node.pop(0))
    # 맨 처음 시작하는 것부터 먼저 시작
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            for i in arr[node]:
                a = solution(i, visited)
                if a == True:
                    queue.append(i)
        if not queue:
            if not start_node:
                continue
            else:
                queue.append(start_node.pop(0))
    return visited

for test_case in range(1, 11):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    list_a = list(map(int, input().split()))
    for i in range(1,len(list_a),2):
        a, b = list_a[i-1], list_a[i]
        arr[a].append(b)

    list_c = [] # 제일 처음 시작하는 노드를 확인하기 위한 대조군
    for i in arr:
        list_c.extend(i)

    # 처음 시작하는 노드 확인
    start_node = []
    for i in range(1, V+1):
        if i not in list_c:
            start_node.append(i)

    print(f'#{test_case} {" ".join(map(str,bfs()))}')

