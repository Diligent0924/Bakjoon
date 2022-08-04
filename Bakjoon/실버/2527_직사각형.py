for _ in range(4):
    x1, y1, x2, y2, r1, t1, r2, t2 = map(int,input().split())
    max_1, min_1, max_2, min_2 = max(x1,r1) , min(x2,r2), max(y1,t1), min(y2,t2)
    if (min_1 - max_1 > 0) and (min_2 - max_2 > 0):
        print("a")
    elif (min_1 - max_1 < 0) or (min_2 - max_2 < 0):
        print("d")
    elif (min_1 - max_1 == 0) and (min_2 - max_2 == 0):
        print("c")
    else:
        print("b")
    

