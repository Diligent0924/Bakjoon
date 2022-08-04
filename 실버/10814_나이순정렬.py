# 1. 나이순으로 정렬
N = int(input())
Dic = {}
list_a = []
for i in range(N):
    a, b = map(str,input().split())
    a = int(a)
    if a in list_a:
        Dic[a].append(b)
    else:
        Dic[a] = [b]
    list_a.append(a)

list_a.sort()

for i in list_a:
    print(i,Dic[i][0])
    Dic[i].pop(0)