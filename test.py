import re


T = int(input())

for _ in range(T):
    # N : 문서의 개수 / M : 원하는 사람 => 위치가 어디인가?
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))
    arr_2 = [[i,v] for i,v in enumerate(arr)]
    arr_2 = sorted(arr_2, key=lambda x: (-x[1], x[0]))
    
    count = 0
    for i in arr_2:
        count += 1
        if i[0] == M:
            print(count)