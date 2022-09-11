import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
copy_arr = [0] * N
for i in range(N):
    copy_arr[i] = arr[i]
copy_arr.sort()

Dic = {}
count = -1
for i in copy_arr:
    if i not in Dic:
        count += 1
        Dic[i] = count # 이부분을 index로 가져오는게 아니라 count로 더해주니까 되었다.

result = [0] * N
for i in range(N):
    result[i] = Dic[arr[i]]
print(*result)