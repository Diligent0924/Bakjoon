'''
2개의 arr를 만들고 같은지 확인한 후에 최댓값을 찾는 방식이 가장 적절하다.
'''
def solution(arr_1, arr_2):
    global count
    arr_1.sort()
    arr_2.sort()
    if arr_1 == arr_2:
        if len(arr_1) > count:
            count = len(arr_1)
            result = arr_1
        return
    else:
        for i, j in graph:
            arr_1.append(i)
            arr_2.append(j)
            solution(arr_1, arr_2)
N = int(input())
graph = [[i for i in range(1,N+1)]]
graph.append([int(input()) for _ in range(N)])
count = 0
result = 0
for i,j in graph:
    solution([i],[j])
print(result)