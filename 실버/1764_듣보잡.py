no_listen, no_see = map(int,input().split())

no_listen_arr = [input() for _ in range(no_listen)]
no_see_arr = [input() for _ in range(no_see)]

result = sorted(list(set(no_listen_arr) & set(no_see_arr)))
print(len(result))
for i in result:
    print(i)