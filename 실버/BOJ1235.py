N = int(input())
list_a = []
list_a = [input()[::-1] for _ in range(N)]
len_word = len(list_a[0])

for i in range(len_word):
    ver = True
    list_b = []
    for j in range(N):
        str1 = list_a[j][:i]
        if str1 in list_b:
            ver = False
            break
        else:
            list_b.append(str1)
           
    if len(list_b) == N:
        print(i)
        break