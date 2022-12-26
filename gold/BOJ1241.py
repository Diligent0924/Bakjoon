import sys
input = sys.stdin.readline
N = int(input())
Dic = {}
result = []
for i in range(N):
    a = int(input())
    result.append(a)

for i in result:
    count = 0
    if i in Dic:
        print(Dic[i])
    else:
        for j in result:
            if i % j == 0:
                count += 1
        Dic[i] = count-1
        print(count-1)