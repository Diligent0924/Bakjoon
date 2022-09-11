'''
DP로만 문제를 풀 수 있다고 한다. => 이해가 안간다.
'''

def solution(i, count):
    if i > N-1:
        return
    elif i == N-1:
        count += arr[i]
        result.append(count)
        result_2.append(arr[i])
        return
    else:
        count += arr[i]
        result_2.append(arr[i])
        solution(i+1, count)
        solution(i+2, count)



N = int(input())
arr = [int(input()) for _ in range(N)]

count = 0
result = []
result_2 = []
solution(0, count)
print(result)
print(result_2)
