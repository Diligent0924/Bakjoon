N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = 0

while B:
    index_min = A.index(min(A))
    index_max = B.index(max(B))
    result += A.pop(index_min) * B.pop(index_max)

print(result)