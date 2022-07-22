N = int(input())
Dic = {}
for i in range(N):
    a , b = map(int, input().split())
    Dic[a] = b
Dic_max = 0
for i in Dic:
    Dic_max = max(Dic_max, Dic[i])
count = 0
for i in range(1,Dic_max+1):
    min_a,max_a = 1000,0
    for key,value in Dic.items():
        if value >= i:
            min_a = min(min_a,key)
            max_a = max(max_a,key)
    count += max_a-min_a+1
print(count)