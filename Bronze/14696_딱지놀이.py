# 1 => 세모 , 2 => 네모, 3 => 동그라미, 4 => 별
from collections import Counter
result = []
for i in range(int(input())):
    list_a = Counter(list(map(int,input().split()))[1:])
    list_b = Counter(list(map(int,input().split()))[1:])
    
    for i in range(4,0,-1):
        if list_a[i] == list_b[i]:
            if i == 1:
                result.append("D")
        elif list_a[i] > list_b[i]:
            result.append("A")
            break
        else:
            result.append("B")
            break
for i in result:
    print(i)    