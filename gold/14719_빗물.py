sero, garo = map(int, input().split())
arr = list(map(int, input().split()))

# 가로 방식으로 점점 올라가는 방법이 제일 좋은듯!
result = 0 # 최종 빗물
for i in range(1,sero+1): # 1층부터 시작한다고 생각해야함
    start, end = -1, -1
    for j in range(garo): # 제일 앞 쪽 확인
        if arr[j] >= i:
            start = j
            break
    for j in range(garo-1,-1,-1): # 가장 뒤쪽 확인
        if arr[j] >= i:
            end = j
            break
    count = 0
    if start == -1 or end == -1: # 만약 정상이라면 끝낸다.
        break
    for j in range(start+1,end): # 그 사이에 있는 물이 있으면 추가해준다.
        if arr[j] < i:
            count += 1
    print(count)
    result += count
print(result)