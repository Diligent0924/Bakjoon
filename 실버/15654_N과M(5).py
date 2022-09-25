def permutation(root):
    if root == M:
        print(*temp)
        return
    else:
        for number in range(len_arr):
            if visited[number]:
                continue
            else:
                visited[number] = 1
                temp[root] = arr[number]
                permutation(root+1)
                visited[number] = 0


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
len_arr = len(arr)
temp = [0] * M
visited = [0] * (N+1)
permutation(0)