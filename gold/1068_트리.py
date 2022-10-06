def preorder(n):
    global count, M
    if n == M: # 해당 부분이 잘라야하는 곳이라면 자른다.
        return

    if not root[n]: # 자식이 없는 노드라면 마지막이기 때문에 더해준다.
        count += 1
        return
    else:
        if len(root[n]) == 1 and root[n][0] == M:
            count += 1
            return
        for i in range(len(root[n])):
            preorder(root[n][i])
            
        
N = int(input())
arr = list(map(int, input().split()))
root = [[] for _ in range(N+1)]
for i in range(N):
    if arr[i] == -1:
        continue
    else:
        root[arr[i]].append(i)

M = int(input())
# print(root)
count = 0
for i in range(N):
    if arr[i] == -1: # root가 0이 아닐 때도 있다.
        preorder(i)
print(count)