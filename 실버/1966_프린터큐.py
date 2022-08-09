T = int(input())

for _ in range(T):
    # N : 문서의 개수 / M : 원하는 사람 => 위치가 어디인가?
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))
    arr_2 = [[i,v] for i,v in enumerate(arr)]
    
    while True:
        max_a = arr_2[0][1]
        for i in range(len(arr_2)):
            if i[1] > max_a:
                max_a = i[1]
                arr_2.append(arr_2.pop(0))
                break
        
        if 
            