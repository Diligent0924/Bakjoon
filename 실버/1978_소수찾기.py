N = int(input())
arr = list(map(int, input().split()))
count = 0
for i in arr:
    list_a = list(map(lambda x : i % x, range(2,i))) # 해당 값을 나눴을 때 0이 나오면 소수가 아님
    if 0 in list_a: # 소수가 아닌 것을 가져옴
        count += 1

if 1 in arr:
    print(N-count-1)
else:
    print(N-count)