'''
부분집합 함수에 대한 암기가 필요할 것 같다.
'''

def subset():
    for i in range(1 << len(arr)):
        result = []
        for j in range(len(arr)):
            if i & (1 << j):
                result.append(arr[j])
        if sum(result) == 100 and len(result) == 7:
            return result


arr = []
for i in range(9):
    arr.append(int(input()))

a = subset()
a.sort()
for i in a:
    print(i)
