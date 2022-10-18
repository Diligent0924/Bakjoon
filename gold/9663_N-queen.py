def queen(root):
    global count
    if root == N: #만약 root가 1일 경우에
        count += 1
        return
    else:
        for i in range(N):
            if graph[root][i]: #만약 방문한 경험이 있다면 다음으로 넘어간다.
                continue
            else: # 방문한 경험이 없다면 해당 부분을 2로 두고 진행한다.
                graph[root][i] = 2
                c = 0
                while c < N:
                    c += 1
                    if root + c < N and not graph[root+c][i]: # 세로축으로 된 부분은 1로 둔다.
                        graph[root+c][i] = root+1
                    if i + c < N and root+c < N and not graph[root+c][i+c]: # 대각선 오른쪽의 경우 1로 둔다.
                        graph[root+c][i+c] = root+1
                    if i - c >= 0 and root+c < N and not graph[root+c][i-c]: # 대각선 왼쪽의 경우를 1로 둔다.
                        graph[root+c][i-c] = root+1                  

                queen(root+1)

                graph[root][i] = 0
                c = 0
                while c < N:
                    c += 1
                    if root + c < N and graph[root+c][i] == root+1: # 세로축을 0으로 둔다.
                        graph[root+c][i] = 0
                    if i + c < N and root+c < N and graph[root+c][i+c] == root+1:
                        graph[root+c][i+c] = 0
                    if i - c >= 0 and root+c < N and graph[root+c][i-c] == root+1:
                        graph[root+c][i-c] = 0


N = int(input())
graph = [[0] * N for _ in range(N)]
count = 0
queen(0)
print(count)