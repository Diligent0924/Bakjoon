N = int(input())
list_a = []
for i in range(N):
    list_a.append(float(input()))

value = 0
while True:
    value += 1
    for i in list_a:
        if not float(i*value).is_integer() or (i*value) % 1 == 9:
            break
    else:
        print(value)
        exit()