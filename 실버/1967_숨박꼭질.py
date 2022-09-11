'''
전형적인 DP 문제이다. => 1부터 10만까지 가장 빠른 겨우의 수를 구하면 된다.
N = 5
'''

N, M = map(int, input().split())
DP = [0] * (abs(N-M))
DP[0] = 1
DP[1] = 2
for i in range(len(DP)):
    if i % N == 0:
        DP[i] = 1

print(DP)
# print(abs(N-M)//N + abs(N-M)%N)
# print(abs(N-M)//N + 1 + N - abs(N-M)%N)
print(min(abs(N-M)//N + abs(N-M)%N, abs(N-M)//N + 1 + N - abs(N-M)%N))