'''
stack을 사용할 수 있는지를 확인하는 문제인것 같다.
'''
N = int(input())
arr = []
for _ in range(N):
    a = int(input())
    if a != 0:
        arr.append(a)
    else:
        arr.pop()
print(sum(arr))