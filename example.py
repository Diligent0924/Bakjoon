T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
		
		# 해당 점에서 양쪽 4분면
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    a = 0
    k = 1
    i = j = 0
		# 
    while k <= N * N:
				# 위치에서 벗어나지 않는다면
        if 0 <= i < N-1 and 0 <= j < N and arr[i][j] == 0:
                arr[i][j] = k
                k += 1
                i += di[a % 4]
                j += dj[a % 4]
        elif 0 < i < N-1 and 0 <= j <= N and arr[i][j] == 0:
                arr[i][j] = k
                k += 1
                i += di[a % 4]
                j += dj[a % 4] 
        elif 0 <= i < N-1 and 0 <= j <= N and arr[i][j] == 0:
                arr[i][j] = k
                k += 1
                i += di[a % 4]
                j += dj[a % 4] 
        elif 0 <= i < N-1 and 0 <= j <= N and arr[i][j] == 0:
                arr[i][j] = k
                k += 1
                i += di[a % 4]
                j += dj[a % 4]        
        else:
						# 이전 while에서 이미 +를 해서 넘쳤기 때문에 다시 돌려야한다.
            i -= di[a % 4]
            j -= dj[a % 4]
            a += 1
            i += di[a % 4]
            j += dj[a % 4]
    print(f'#{t}')
    for i in arr:
        print(*i)