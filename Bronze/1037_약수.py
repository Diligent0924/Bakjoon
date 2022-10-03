'''
N : 약수의 개수
list : 진짜 약수
'''

N = int(input())
list_a = list(map(int, input().split()))
max_count = max(list_a)
i = 1
while True:
    i += 1
    break_i = True
    temp_count = max_count * i
    for j in list_a:
        if temp_count % j != 0:
            break_i = False
            break

    if break_i == False:
        continue
    else:
        print(temp_count)
        break    