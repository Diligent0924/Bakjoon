'''
결과물 : 장애물의 최솟값, 구간의 개수 구하기!!
'''
#from pprint import pprint
import sys
input = sys.stdin.readline
N, H = map(int, input().split())

arr = []
prefix = [0] * H
for _ in range(N):
    arr.append(int(input()))

for i in range(N):
    if not i % 2:
        prefix[0] += 1
        prefix[arr[i]] += -1
    else:
        prefix[(H-1)-arr[i]+1] += 1
    # print(prefix)        
for i in range(1,H):
    prefix[i] = prefix[i-1] + prefix[i]
    
# print(prefix)
count = 0
a = min(prefix)
for i in prefix:
    if i == a:
        count += 1
print(a, count)