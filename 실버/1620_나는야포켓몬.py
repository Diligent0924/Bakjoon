import sys
N, M = map(int,sys.stdin.readline().strip().split())
arr = {i:input() for i in range(N)}
arr_2 = {}
for i,v in arr.items():
    arr_2[v] = i

for _ in range(M):
    answer = sys.stdin.readline().strip()
    # print(f'??? {answer} {answer[0]}')
    if answer[0] in ("0","1","2","3","4","5","6","7","8","9"):
        print(arr[int(answer)-1])
    else:
        print(arr_2[answer]+1)