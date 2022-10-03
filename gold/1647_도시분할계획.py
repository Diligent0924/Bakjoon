def find_set(x):
    while x != standard[x]:
        x = standard[x]
    return x

N = int(input())
M = int(input())
db = []
for _ in range(M):
    u,v,w = map(int, input().split())
    db.append((w,u,v))

db.sort()
standard = [i for i in range(N+1)]
cnt = 0
total = 0
for w,u,v in db:
    if find_set(u) != find_set(v):
        cnt += 1
        total += w
        standard[find_set(v)] = find_set(u)
        if cnt == N:
            break
print(total)