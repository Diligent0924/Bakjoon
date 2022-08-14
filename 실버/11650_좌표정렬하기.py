'''
    lambda를 이용한 문제풀이 방법
    lambda로 여러가지 Customizing Sorting이 가능하다.
'''

import sys
N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr.append([a,b])

arr = sorted(arr, key=lambda x: (x[0],x[1]))

for i in arr:
    print(*i)