# .sort() 나 sorted()는 가장 빠른 정렬방법 모듈이다.
import sys
arr = []
for _ in range(1,int(sys.stdin.readline())+1):
    arr.append(int(sys.stdin.readline()))

arr.sort()
for i in arr:
    print(i)