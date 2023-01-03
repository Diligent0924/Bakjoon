N = int(input())
M = int(input())
candidate = list(map(int, input().split()))
list_a = []

for i in candidate: # 추천 후보들을 한명씩 보낸다.
    for j in list_a: # list_a 내를 돌아봤을 때
        if i == j[0]: # 만약 있다면
            j[1] += 1
            break
    else: # 만약 없다면
        if len(list_a) == N: # 만약 N과 같다면...
            min_a = 100000000
            min_index = -1
            for j in range(N):
                if list_a[j][1] < min_a:
                    min_a = list_a[j][1]
                    min_index = j
            list_a.pop(min_index)
        list_a.append([i,1]) # i가 1개 들어있다는 것을 넣어준다.

list_a.sort(key = lambda x: x[0])
for i in list_a:
    print(i[0], end= " ")