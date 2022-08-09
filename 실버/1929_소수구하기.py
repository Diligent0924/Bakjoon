# 무슨 이상한 공식 써야함..
a, b = map(int, input().split())
if a % 2 == 0:
    for i in range(a+1,b,2):
        arr = list(map(lambda x: i % x, range(1,i,2)))
        if arr.count(0) < 2:
            print(i)
else:
    for i in range(a,b,2):
        arr = list(map(lambda x: i % x, range(1,i,2)))
        if arr.count(0) < 2:
            print(i)
