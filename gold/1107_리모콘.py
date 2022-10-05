def solution(now):
    global number, result
    for i in str(now):
        if i not in number:
            return
    # 만약 더 작으면
    if abs(N-result) > abs(N-now):
        result = now
        return
        
N = int(input())
M = int(input())
origin_number = set(["0","1","2","3","4","5",'6',"7","8","9"])
if not M:
    number = list(origin_number)
else:
    arr = set(input().split())
    number = list(origin_number - arr)

now = -1 # 현재 위치
result = -10000
while now < 1000000:
    now += 1
    solution(now)

# print(result)
count = 0
for i in str(result):
    count += 1

count += abs(N - result)
answer = min(count, abs(N-100))
print(answer)