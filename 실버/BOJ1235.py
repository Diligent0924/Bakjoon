import sys
N = int(input())
list_a = [input()[::-1] for _ in range(N)]
len_word = len(list_a[0])

for i in range(1,len_word+1):
    list_b = []
    for j in range(N):
        str1 = list_a[j][:i]
        if str1 in list_b:
            break
        else:
            list_b.append(str1)
    # print(list_b)         
    if len(list_b) == N:
        print(i)
        break