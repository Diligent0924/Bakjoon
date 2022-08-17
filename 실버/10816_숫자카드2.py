'''
Collections.Counter를 사용할 수 있냐의 문제이다.
'''

N = int(input())
arr_1 = list(map(int, input().split()))
M = int(input())
arr_2 = list(map(int, input().split()))

from collections import Counter
arr_1 = Counter(arr_1)

for i in arr_2:
    print(arr_1[i], end=' ')