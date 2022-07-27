N = int(input())

if (N == 1 or N == 2):
    print(N)
else:
    list_a = list(map(int, input().split()))
    max_length,count_1,count_2 = 0, 1, 1
    for i in range(len(list_a)-1):
        # 오름차순
        if list_a[i] >= list_a[i+1]:
            count_1 += 1
            max_length = max(max_length, count_1)
        else:
            count_1 = 1
        #내림차순
        if list_a[i] <= list_a[i+1]:
            count_2 += 1
            max_length = max(max_length,count_2)
        else:
            count_2 = 1  
    print(max_length)