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
