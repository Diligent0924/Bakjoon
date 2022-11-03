N = int(input())
trees = list(map(int, input().split()))
growth = list(map(lambda x: int(x), input().split()))

result = 0
time = N-1
while time != -1:
    print(result)
    print(trees)
    print(growth)
    max_index = -1
    max_count = -1
    for i in range(time+1):
        a = trees[i] + growth[i] * time 
        if a > max_count:
            max_count = a
            max_index = i
    trees.pop(max_index)
    growth.pop(max_index)
    time -= 1
    result += max_count
print(result)