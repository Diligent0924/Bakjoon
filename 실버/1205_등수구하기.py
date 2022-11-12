N, score, P = map(int, input().split())
if not N:
    print(1)
else:
    arr = list(map(int, input().split()))
    for i in range(N):
        if (arr[i] < score and i+1 <= P) or (arr[i] == score and i+arr.count(arr[i])+1 <= P):
            print(i+1)
            break
        elif i == N-1 and arr[i] > score and N+1 <= P:
            print(i+2)
            break
    else:
        print(-1)