'''
과제 최근 순 => 과제 도중 새로운 과제 오면 새로운 과제 => 새로운 과제가 끝나면 이어서 한다.
'''
import sys
input = sys.stdin.readline
N = int(input())
result = 0
list_a = []
for _ in range(N):
    a = list(map(int,input().split()))
    b = a.pop(0)
    if b:
        list_a.append([a[0],a[1]])
        list_a[-1][1] -= 1
    elif list_a and not b:
        c,d = list_a.pop()
        d -= 1
        list_a.append((c,d))
    
    if list_a and not list_a[-1][1]:
        result += list_a[-1][0]
        list_a.pop()

print(result)
