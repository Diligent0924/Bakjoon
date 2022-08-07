N = int(input())

list_a = [int(input()) for _ in range(N)]
list_b = []
result = []
for i in range(1,N+1):
    list_b.append(i)
    # print(list_a,list_b)
    result.append("+")
    while True:
        if len(list_a) == 0 or len(list_b) == 0:
            break
        elif list_b[-1] == list_a[0]:
            result.append("-")
            list_b.pop()
            list_a.pop(0)
            # print(list_a,list_b)
        # elif list_b[-1] > list_a[0]:
        #     if list_a[0] in list_b:
        #         list_b.pop()
        #         list_a.pop(0)
        #     else:
        #         print("NO")
        else:
            break

if len(list_a) > 0:
    print("NO")
else:
    for i in result:
        print(i)