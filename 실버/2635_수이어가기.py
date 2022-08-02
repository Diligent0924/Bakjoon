N = int(input())
count,result_1,result_2 = 0,0, []
while count < N:
    count += 1
    list_a = [N, count]
    while True:
        if list_a[-2] - list_a[-1] < 0:
            if len(list_a) > result_1:
                result_1 = len(list_a)
                result_2 = list_a
            break
        else:
            list_a.append(list_a[-2] - list_a[-1])

print(result_1)
print(' '.join(map(str, result_2)))