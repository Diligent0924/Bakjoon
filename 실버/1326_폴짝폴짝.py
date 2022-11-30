'''
DP 문제라고 보여진다.
 => 그 전에 있던 얘들 중에서 count를 해서 계속 지나가면 되지 않을까?
 a > b일 경우에도 있지 않을까? => 있을듯 ㄷ;;
'''

N = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())
DP = [-1] * (N+1) # 모든 수를 -1로 두고 시작한다.

if a > b: # 만약 더 큰 경우에는 arr를 변환해서 사용한다.
    a, b = b, a
    arr.reverse()
arr = [0] + arr
DP[a] = 0 # 처음인 경우에는 찾을 수 있어야 한다.
for i in range(a+1, N+1): # 시작하는 곳 뒤에서부터 마지막까지를 확인한다.
    min_index = 0
    min_count = 10000000
    for j in range(a,i): # 그 전까지 중에서 조건에 맞는 것이 있는지를 먼저 파악한다.(개구리가 뛸수있는 거리여야한다.)
        if DP[j] <= min_count and not (i-j) % arr[j] and DP[j] != -1: # 되는것을 일단 먼저 찾는다.
            min_index = j
            min_count = DP[j]
            
    if not min_index: # 만약 아예 못가는 장소라면 그대로 둔다.
        DP[i] = -1
    else: # 최소의 것에서 하나씩을 더한다.
        DP[i] = DP[min_index] + 1
# print(DP)
print(DP[b])