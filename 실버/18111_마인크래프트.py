'''
1층일 떄 해당 수를 저장한다.
2층일 때 1층 + 나머지 수를 추가해서 계속 집어넣는다.
'''
import sys
N, M, B = map(int, sys.stdin.readline().split()) # N : 가로, M : 세로, B :가지고 있는 블록 수
arr = [] # 500 * 500 => 250000번
for i in range(N):
    arr.extend(list(map(int, sys.stdin.readline().split())))
min_a = float('inf') # 정수
min_index_i = 0
count_list = []
count = 0
for i in range(min(arr),max(arr)+1): # 아무리 커도 257
    count_1,count_2 = 0,0
    
    B_1 = B
    for j in arr: # 최대 250000번
        if i > j:
            count_1 += (i-j)
            B_1 -= i-j
        else:
            count_2 += (j-i)
            B_1 += j-i

    if B_1 < 0:
        continue
    else:
        if count_1 + 2 * count_2 <= min_a:
            min_a = count_1 + 2* count_2
            min_index_a = i

print(min_a, min_index_a)