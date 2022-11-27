N, M = map(int, input().split())
package = []
seperate = []
# 패캐기와 각각
for _ in range(M):
    a, b = map(int, input().split())
    package.append(a)
    seperate.append(b)

print(min(min(package)*(N//6+1), min(package)*(N//6) + min(seperate) * (N%6),min(seperate) * N))
