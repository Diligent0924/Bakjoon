N, r, c = map(int,input().split()) # N : 정사각형 길이 / r: 찾는행(세로) / c: 찾는열(가로)
def solution(arr):
    global N
    if len(arr) == 2:
        result.append([0] * 2)
        return
    else:
        N -= 1
        solution(arr)
        
arr, result = [],[]
for _ in range(4):
    arr.append([[0] * (2**(N-1)) for _ in range(2**(N-1))])

print(arr)
