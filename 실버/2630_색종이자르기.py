def partition(first_i, first_j, box_size):
    global result
    # print(first_i,first_j)
    number = graph[first_i][first_j]
    if box_size == 1:
        if number == 0:
            result[0] += 1
        else:
            result[1] += 1
        return
    else:
        for i in range(first_i, first_i+box_size):
            for j in range(first_j, first_j+box_size):
                if graph[i][j] != number:
                    partition(first_i, first_j, box_size//2)
                    partition(first_i, first_j+box_size//2, box_size//2)
                    partition(first_i+box_size//2, first_j, box_size//2)
                    partition(first_i+box_size//2, first_j+box_size//2, box_size//2)
                    return
        else:
            if number == 0:
                result[0] += 1
            else:
                result[1] += 1
            return

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
result = [0, 0]
partition(0,0,N)
for i in result:
    print(i)