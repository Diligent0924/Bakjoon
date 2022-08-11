# 노가다하면 x는 4 - 5 - 6 - 5 - 4 - 3- 2 - 1- 0 - 1 - 2 -3(12개)
# y는 1 - 2 - 3 - 4- 3 - 2 -1 - 0(8개)로 반복되어 나온다.
size_x, size_y = map(int,input().split())
x, y = map(int,input().split())
t = int(input())

if (x+t) % (2*size_x) > (size_x):
    a = 2 *size_x - ((x+t) % (2*size_x))
else:
    a = (x+t) % (2*size_x)

if (y+t) % (2*size_y) > (size_y):
    b = 2 * size_y - ((y+t) % (2*size_y))
else:
    b = (y+t) % (2*size_y)

print(a, b)