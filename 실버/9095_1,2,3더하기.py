'''
재귀함수로 풀면 빠르게 풀 수 있지 않을까 싶다.
'''
def solution(n):
    global count
    if n > r:
        return
    elif n == r:
        count += 1
        return
    else:
        solution(n+1)
        solution(n+2)
        solution(n+3)

N = int(input())
for _ in range(N):
    r = int(input())
    count = 0
    solution(0)
    print(count)