'''
 count 정렬에 대하여 알게 되었다.
 sort()와는 다르게 어떤 입력된 수 등을 정렬할 떄는 더 빠른거 같다!
'''

import sys
N = int(sys.stdin.readline())
# arr = []
# for _ in range(N):
#     arr.append(int(sys.stdin.readline()))

# arr = sorted(arr)
# for i in arr:
#     print(i)


arr = [0] * 10001
for _ in range(N):
    arr[int(sys.stdin.readline())] += 1


for i in range(10001):
    if arr[i] > 0:
        for j in range(arr[i]):
            print(i) # 바로 프린트하면 메모리가 줄어든다!