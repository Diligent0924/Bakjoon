# 붙어있는 숫자는 같아야한다.
# 4면 중 어느 한면의 숫자의 합이 최대

N = int(input())
list_a = [list(map(int, input().split())) for _ in range(N)]
max_a = []
for j in range(1,7):
    result= []
    for i in list_a:
        if i.index(j) == 0 or i.index(j) == 5:
            result.append(i[1:5])
            continue
        elif i.index(j) == 1 or i.index(j) == 3:
            result.append([i[0],i[2],i[4],i[5]])
            continue
        elif i.index(j) == 2 or i.index(j) == 4:
            result.append([i[0],i[1],i[3],i[5]])
            continue

        count_1 = 0
        for i in result:
            count_1 += max(i)
        max_a.append(count_1)
        print(count_1)