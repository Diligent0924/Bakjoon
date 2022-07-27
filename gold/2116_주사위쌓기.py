N = int(input())
list_a = [list(map(int, input().split())) for _ in range(N)]
max_a = []
for i in range(1,7):
    result,count_1,b = [], 0, i
    for j in list_a:
        if j.index(b) == 0:
            result.append(j[1:5])
            b = j[5]
        elif j.index(b) == 5:
            result.append(j[1:5])
            b = j[0]          
        elif j.index(b) == 1:
            result.append([j[0],j[2],j[4],j[5]])
            b = j[3]
        elif j.index(b) == 3:
            result.append([j[0],j[2],j[4],j[5]])
            b = j[1]   
        elif j.index(b) == 2:
            result.append([j[0],j[1],j[3],j[5]])
            b = j[4] 
        elif j.index(b) == 4:
            result.append([j[0],j[1],j[3],j[5]])
            b = j[2]
            
    for i in result:
        count_1 += max(i)
    max_a.append(count_1)
print(max(max_a))