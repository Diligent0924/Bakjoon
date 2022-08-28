'''
전체 크기 정사각형 => 그 안에 각자의 물질 박스 직사각형
물질 박스는 반드시 가운데 사이에 0이 1개 이상은 있어야한다.

출력 : 개수 + 행렬들의 행과 열을 출력(크기가 작은 순으로)
문제풀이
1. visited를 따로 만들어서 방문한 곳을 파악하기 (각 개수마다 초기화)\
2. visited에서 해당 섬의 행과 열을 확인하기
3. 진짜 graph에서 해당 visited를 0으로 만들어주기
'''
def solution(sero,garo):
    visited = [[0] * N for _ in range(N)]
    queue = []
    queue.append((sero,garo))
    arr[sero][garo] = 0
    visited[sero][garo] = 1
    result_list = []
    result_list.append((sero,garo))
    while queue:
        i, j = queue.pop(0)
        for di, dj in ([0,1], [0,-1], [-1,0], [1,0]):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 0 and visited[ni][nj] == 0:
                queue.append((ni,nj))
                arr[ni][nj] = 0 # 원래 있던 자리를 0으로 만들어준다.
                visited[ni][nj] = visited[i][j] + 1
                result_list.append((ni,nj))
    result.sort()
    a, b = result_list[0]
    c, d = result_list[-1]
    return c-a+1, d-b+1

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    result = []
    for sero in range(N):
        for garo in range(N):
            if arr[sero][garo] != 0:
                count += 1
                result.append(solution(sero, garo))

    result = sorted(result, key=lambda x: x[0]*x[1])
    print(f'#{test_case} {count}', end=' ')
    for i in result:
        print(*i, end=" ")
    print()
