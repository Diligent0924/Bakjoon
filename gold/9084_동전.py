'''
동전이 갈 수 있는 방법의 수를 앞에서부터 확인하는 DP 방식을 이용!
Combination 개념이기 때문에 cost를 먼저 for문 돌려야 한다! (그래야 개수를 확인할 수 있다.)
'''
import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    N = int(input()) # 동전의 가지 수
    costs = list(map(int,input().split()))
    M = int(input())
    dp = [0] * (M+1) # 해당 위치까지 가위한 방법을 정의한다.
    # print(dp)
    for j in costs:
        if j in costs and j <= M:
            dp[j] += 1
        for i in range(1,M+1):
            if i-j >= 0:
                dp[i] += dp[i-j]
    print(dp[-1])