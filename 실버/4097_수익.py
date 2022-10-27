while True:
    N = int(input())
    if not N:
        break
    else:
        # 입력을 먼저 받는다.
        arr = [int(input()) for _ in range(N)]

        # 만약 모든 arr의 값이 0보다 작다면 가장 arr중에서 가장 큰 값을 가져온다.
        break_i = True
        for i in arr:
            if i >= 0: # 만약 0보다 큰값이 하나라도 존재한다면 dp를 확인한다.
                break_i = False 
                break
        else:
            print(max(arr))

        # 0이상인 수가 1개 이상일 경우
        if not break_i:
            dp = []
            dp.append(max(0,arr[0]))
            for i in range(1, N):
                a = max(max(0,arr[i]), dp[-1] + arr[i])
                dp.append(a)
            print(max(dp))
