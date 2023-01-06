N = int(input())
arr = [int(input()) for i in range(N)]
podoju = [0] * N # N개의 일렬로 정의된 포도주들
podoju[0] = arr[0]
podoju[1] = arr[0] + arr[1]

for i in range(2, len(arr)): # 해당 인덱스 값이 되었을 경우 
    podoju[i] = podoju[i-2] + arr[i]
print(podoju)
