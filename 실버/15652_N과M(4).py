def permutation(root):
    if root == M:
        print(*temp)
        return
    else:
        for number in range(temp[root-1], N+1): # 그전에꺼보다는 같거나 커야되는 수가 들어가야 하기 때문에
            visited[number] = 1
            temp[root] = number
            permutation(root+1)
            visited[number] = 0

N, M = map(int, input().split())
temp = [1] * M
visited = [0] * (N+1)
permutation(0)