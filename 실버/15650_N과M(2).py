def permutation(root):
    if root == M:
        sorted_a = sorted(temp)
        # print(f'sorted : {sorted_a}')
        if sorted_a == temp:
            print(*temp)
    else:
        for number in range(1, N+1):
            if visited[number]:
                continue
            else:
                visited[number] = 1
                temp[root] = number
                permutation(root+1)
                visited[number] = 0


N, M = map(int, input().split())
temp = [0] * M
visited = [0] * (N+1)
permutation(0)