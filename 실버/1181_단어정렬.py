# lambda에 대한 여러가지 사용방법
# sorted + lambda 방법 => sorted(list, key = lambda x: ...) 방식으로 사용할 수 있다.
# 만약 여러가지 조건에서 사용하고 싶다면 key = lambda x: (a,b) 방식으로 사용하면 가능하다.
list_a = []
N = int(input())
for i in range(N):
    list_a.append(input())

list_a = sorted(list(set(list_a)), key=lambda x: (len(x),x))
for i in list_a:
    print(i)