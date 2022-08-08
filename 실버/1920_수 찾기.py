# sorted가 되는 list에서 어떠한 특정 수를 찾을 때 사용하는 방법 => 이분탐색
# 이분탐색에 대해서 좀 더 정확히 알 필요가 있다.
# 쓸데없이 너무 많은 list를 소모시킨다. => 코드 자체를 클린하게 짜야한다.
N_1 = int(input())
arr_1 = sorted(list(map(int, input().split())))
N_2 = int(input())
arr_2 = list(map(int, input().split()))
for i in arr_2:
    start, end = 0, N_1-1 # 이부분에서 틀렸다 (N_1 -1을 하는 이유: list를 기준으로 index에 들어갈 것이므로)
    while start <= end: # start <= end이여야 반드시 start > end이기 때문에
        #print(f'start {start} end {end}')
        mid = (start + end) // 2
        #print(f'mid {mid}')
        if i > arr_1[mid]:
            start = mid+1
        elif i < arr_1[mid]:
            end = mid-1
        elif i == arr_1[mid]:
            print(1)
            break
    if start > end:
        print("0")