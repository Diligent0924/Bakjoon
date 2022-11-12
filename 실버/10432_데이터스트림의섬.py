N = int(input())
for _ in range(N):
    arr = list(map(int, input().split()))
    number = arr.pop(0)
    count = 0
    visited = [0] * 12
    for i in range(12):
        # print(visited)
        start = False
        if not visited[i] and arr[i]: # 방문한 곳이 아니면 끝낸다.
            for j in range(i,12):
                if not start and arr[j]: # 처음 시작을 확인
                    start = True
                    visited[i] = 1
                if start and not arr[j] or start and arr[j] < arr[i]:
                    # print(i)
                    count += 1
                    break
                elif start and arr[i] == arr[j]:
                    visited[j] = 1
        
    print(f'{number} {count}')