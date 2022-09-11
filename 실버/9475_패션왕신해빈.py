tc = int(input())
for _ in range(tc):
    N = int(input())
    Dic = {}
    for _ in range(N):
        a, b = input().split()
        if b not in Dic:
            Dic[b] = []
        Dic[b].append(a)

    count = 1
    for i in Dic:
        count *= (len(Dic[i]) + 1)
    print(count-1)
