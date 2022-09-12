'''
문제가 좀 이상하다..??

'''

def num(m, n, x, y):
    while x <= m*n:
        if x % n == y % n: #
            return x
        x += m
    return -1

tc = int(input())
for i in range(tc):
    m, n, x, y = map(int, input().split()) # m, n, x, y =>
    print(num(m,n,x,y))