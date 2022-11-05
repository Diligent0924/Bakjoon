'''
현재에서 갈 수 있는 구간을 추가해서 더하는 방식을 사용한다.
여기에 들어간 인덱스가 2개가 혼합되어 있어서 어려웠음(1시간 소비)
정확하게 문제를 확인하는 습관이 필요함
여기서는 현재 위치에서 어디 위치로 넘어갈 수 있느냐를 묻는 문제였음.
'''


def solution(root,count): # 현재 자신의 위치
    global result
    if root > T:
        return
    else:
        result = max(result, count)
        for i in range(root, T):
            solution(i+work[i], count + pay[i])

T = int(input())
work = []
pay = []
for _ in range(T):
    a,b = map(int, input().split())
    work.append(a)
    pay.append(b)

result = 0
solution(0,0)
print(result)