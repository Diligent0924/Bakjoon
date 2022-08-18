'''
재귀함수를 풀어쓰는 방식에 대하여 알 수 있었다.
재귀함수에 사용하는 것을 앞에 하나하나씩 미리 저장해둔다면 빠르게 풀 수 있다.
'''
list_a = [[1,0],[0,1]] # 미리 밖에 저장함으로써 바로 가져다 쓸 수 있게 한다.
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(input())
    if N < len(list_a): # list_a안에 있다면 바로 답을 출력한다.
        print(list_a[N][0], list_a[N][1])
    else:
        while len(list_a) <= N: # N이 나올 때까지 계속 list_a에 추가한다.
            list_a.append([list_a[-2][0] + list_a[-1][0], list_a[-2][1] + list_a[-1][1]])
        print(list_a[-1][0], list_a[-1][1])