# 기본적으로 문제를 풀 때 너무 급한 성격이므로 성격을 줄이고 푸는 것이 도움이 될듯 싶다.
# SWEA의 색종이 문제와 비슷하며 이러한 행열로 찍을 때는 y축을 먼저 for문 돌려야된다. => 매우 중요
graph = [[0]*1000 for _ in range(1000)]
for i in range(4):
    a,b,c,d = map(int,input().split())
    for n in range(b,d):
        for m in range(a,c):
            graph[n][m] = 1
count_a = 0 
for i in graph:
    count_a += i.count(1)
print(count_a)