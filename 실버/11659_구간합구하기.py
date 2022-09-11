'''
DP로 미리 합을 구한뒤에 해당 값에서 뺴는 방식으로 사용하면 편하다.
=> DP(미리 저장)의 아주 중요한 예시이다.
'''
import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
DP = [0]

for i in arr:
    DP.append(DP[-1] + i)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(DP[b] - DP[a-1])