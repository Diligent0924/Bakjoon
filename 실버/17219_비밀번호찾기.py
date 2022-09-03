N, M = map(int, input().split())
dic = {}
for _ in range(N):
    a, b = map(str, input().split())
    dic[a] = b

for _ in range(M):
    a = input()
    print(dic[a])