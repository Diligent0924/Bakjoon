# 특정 조건을 구하는 것이 중요한 문제이다.

for _ in range(int(input())):
    k = int(input()) # 층
    n = int(input()) # 호
    # 문제에서 1~n까지의 그 전 합이 필요하다 하였으니 처음 0일때를 정해야한다.
    arr = [i for i in range(1,n+1)] 

    for i in range(k): # 층수별로 사용한다.
        for j in range(1,n): # 앞에서부터 바뀌게끔 사용한다.
            arr[j] = arr[j-1] + arr[j]
    print(arr[-1])
    
    ''' 예시
    
    0층 : 1 2 3
    1층 : 1,3,3 (j가 한번 돌때)
    1층 : 1,3,6 (0층의 arr[j] 3 과 앞서 1층의 arr[j-1] 3을 더한다.
    ... (반복)
    
    '''