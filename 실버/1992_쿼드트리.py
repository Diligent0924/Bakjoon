'''
1074_Z 와 비슷한 방식으로 어떤 함수를 전체로 돌릴 때 사용하는 방법...
'''
def partition(start_i, start_j, box_size):
    global word
    if box_size == 1:
        word += str(graph[start_i][start_j])
        return
    else:
        standard = graph[start_i][start_j]
        for i in range(start_i, start_i + box_size):
            for j in range(start_j, start_j + box_size):
                if graph[i][j] != standard:
                    word += "("
                    partition(start_i, start_j, box_size//2)
                    partition(start_i, start_j + box_size//2, box_size//2)
                    partition(start_i + box_size//2, start_j, box_size//2)
                    partition(start_i + box_size//2, start_j + box_size//2, box_size//2)
                    word += ")" # 해당 분면이 종료되는 시점에서 추가해주는 방식인가 봄...
                    return
        else:
            word += str(graph[start_i][start_j])
            return




N = int(input())
graph = [list(input()) for _ in range(N)]
word = ""
partition(0, 0, N)
print(word)