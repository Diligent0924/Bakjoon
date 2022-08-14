'''
 단순히 Greedy로 문제를 푸는 것은 좋지 않다. 
 순열과 조합을 사용하면 편하다.
 itertools에는 combination(조합) / permutation(순열)이 있다.
 combination(조합)은 순서가 없고 permutation은 순서가 있다.
 SWEA에서도 허락해준다..
'''
from itertools import combinations
N, M = map(int, input().split()) # 카드의 개수, 딜러가 말한 수
arr = list(map(int,input().split())) # 받은 카드 수 => 여기서 3개를 골라야함
nCr = list(combinations(arr,3))
min_M = M
for i in nCr:
    if M - sum(i) < min_M and M - sum(i) >= 0:
        min_a = sum(i)
        min_M = M-sum(i) # 자꾸 이부분에서 막혔었다. 
print(min_a)

'''
 min_M을 왜 sum(i)로 계속 둬서 오래걸렸었다.
 max,min을 풀이할 때 풀어쓰는 방법에 대해 좀 더 공부가 필요하다.
 어떤 특정 숫자에 가장 가까운것을 찾을 때와 같이 비교할 때 비교대상을 명확히 확인한다.
'''
