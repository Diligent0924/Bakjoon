for _ in range(4):
    a, b, c, d, e, f, g, h = list(map(int, input().split()))
    max_1 , min_1 = max(a,e), min(c,g)
    max_2, min_2 = max(b,f) , min(d,h)
    
    if min_1 - max_1 > 0 and min_2 - max_2 > 0:
        print("a")
    elif min_1 - max_1 < 0 or min_2 - max_2 < 0:
        print("d")
    elif min_1 - max_1 == 0 and min_2 - max_2 == 0:
        print('c')
    else:
        print('b')