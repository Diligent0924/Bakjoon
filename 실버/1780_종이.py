N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# result = [0,0,0]
# count = 0
# arr_2 = [arr]
# while True:
#     for i in range(len(arr_2)):
#         for j in range(N):
#             for h in range(N):
#                 # arr_2 에서 하나라도 달라지면..
#                 N = N//3
#                 arr_2 = []


    # else:
arr_2 = []
for m in range(2):
    print(N)
    print(N//3)
    for i in range(0,9,N//3):
        list_a = []
        for j in range(0,9,N//3):
            for h in range(i+N//3):
                list_a.append(arr[h][j:j+N//3])
        arr_2.append(list_a)
    N = N//3
print(arr_2)