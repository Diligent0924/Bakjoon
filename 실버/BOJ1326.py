N = int(input())
arr = [0] + list(map(int, input().split()))
a, end = map(int, input().split())
DP = [0] * len(arr) # arr의 개수만큼을 0으로 

real = [a]
result = 0
while True:
    start = real.pop(0)
    arr = []
    for i in range(start+1, len(arr)):
        if not i % DP[start]: # 만약 나머지가 없다면
            arr.append(i)
    if end in arr:
        print(result)
        break
    real.extend(arr)