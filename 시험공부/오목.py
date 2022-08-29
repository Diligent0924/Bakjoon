def solution():
    # 가로로 확인
    for i in range(N):
        count = 0
        for j in range(N):
            if arr[i][j] == 1:
                count += 1
            else: # 0이면 count의 개수를 세고 5를 넘으면 True로 변경한다. 안넘으면 0으로 count를 바꿔준다.
                if count >= 5:
                    return True
                else:
                    count = 0
        if count >= 5: # 끝에 머리에 count의 개수가 5 이상이면 끝낸다.
            return True

    # 세로로 확인
    for i in range(N):
        count = 0
        for j in range(N):
            if arr[j][i] == 1:
                count += 1
            else:
                if count >= 5:
                    return True
                else:
                    count = 0
        if count >= 5:
            return True


    # 대각선으로 확인하기
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                count = 1
                for di ,dj in ((1,1), (2,2), (3,3), (4,4)):
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:
                        count += 1
                        if count == 5:
                            return True
                    else:
                        break

                count = 1
                for di, dj in ((1, -1), (2, -2), (3, -3), (4, -4)):
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:
                        count += 1
                        if count == 5:
                            return True
                    else:
                        break
                else:
                    return True

    return False

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(lambda x: 0 if x == '.' else 1, input())) for _ in range(N)]
    a = solution()
    if a:
        print(f'#{test_case} YES')
    else:
        print(f'#{test_case} NO')

