N = int(input())
if not N:
    print(0)
else:
    n = 0
    count = 0
    while True:
        decrease = True
        n += 1
        value = 10
        for i in str(n):
            v = int(i)
            if v < value:
                value = v # 해당 값으로 변경하고
            else: # 만약 같거나 큰수로 들어온다면..
                decrease = False
                break
        if decrease:
            print(n)
            count += 1
        if count == N:
            print(n)
            break

    # if n == 1000000:
    #     print(-1)