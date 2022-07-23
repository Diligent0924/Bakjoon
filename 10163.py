# 기존에 풀었던 방식은 limit exceed가 나서 터진 것으로 판단된다.
# 100점 기준으로 중간에 멈추게 된다면 memory exceed일 가능성도 있다.
# collections.Counter도 Dic과같은 형태로 나타나므로 확인해보기 좋다.
import collections
N = int(input())
graph = [[0] * 1001 for i in range(1001)]

for i in range(1,N+1):
    a ,b, c, d = map(int,input().split())
    for n in range(b,b+d):
        graph[n][a:a+c] = [i] * c

result = []
for i in graph:
    for j in i:
        result.append(j)

result = collections.Counter(result)
for i in range(1,N+1):
    print(result[i])