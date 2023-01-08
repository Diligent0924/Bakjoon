# DP는 현재의 위치를 먹었을 때의 최댓값으로 구한다.
N = int(input())
arr = [int(input()) for i in range(N)]
# print(arr)
DP = [0] * N # 바로 앞칸으로 한 경우
for i in range(N):
    if i == 0:
        DP[0] = arr[0]
    elif i == 1:
        DP[1] = arr[0] + arr[1]
    elif i == 2:
        DP[2] = max(arr[0], arr[1]) + arr[2]
        DP[2] = max(DP[2],DP[1])
    else: 
        DP[i] = arr[i] + max(DP[i-2], arr[i-1]+DP[i-3])
        DP[i] = max(DP[i], DP[i-1])
# print(DP)
print(max(DP))