N, K = map(int,input().split())
ondos = list(map(int,input().split()))
result = sum(ondos[0:K])
kun_ondos = sum(ondos[0:K])
list_a,start = [], 0
for i in range(N-K):
    start = ondos[i]
    end = ondos[K+i]
    result = result - start + end
    kun_ondos = max(kun_ondos, result)
print(kun_ondos)