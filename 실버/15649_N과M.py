def permutation(root):
    if root == M:
        print(*temp)
        return
    else:
        for i in range(1, N+1):
            if visited[i]:
                continue
            else:
                visited[i] = 1
                temp[root] = i
                permutation(root+1)
                visited[i] = 0


N, M = map(int, input().split())
temp = [0] * M
visited = [0] * (N+1)
permutation(0)