'''
단방향으로 확인이 가능하다.
A, B, C, D를 각각 0, 1과 같이 순서대로 넣는다. ord("A") - 65 방식을 사용
root가 2개인 경우의 수도 있을 수 있다.

'''
def ord_change(alpha):
    return ord(alpha) - 65

def recurse(now):
    queue = [now]
    while queue:
        n = queue.pop(0)
        if not visited[n]:
            visited[n] = 1
            queue.extend(arr[n])

def root():
    number = 0
    root_visited = [0] * 26
    for k in point:
        queue = [k]
        while queue:
            n = queue.pop(0)
            for l in arr[n]:
                if not root_visited[l]:
                    root_visited[l] = 1
                    queue.append(l)
    for k in point:
        if not root_visited[k]:
            number += 1
    # print(root_visited)
    # print(point)
    return number

N, M = map(int, input().split())
arr = [[] for _ in range(26)]
point = set()
for _ in range(M):
    a, b = map(str, input().split())
    arr[ord_change(a)].append(ord_change(b))
    point.add(ord_change(a))
    point.add(ord_change(b))

root_number = root()
print(root_number)

visited = [0] * 26
p_list = list(input().split())[1:]
for p_value in p_list:
    p = ord_change(p_value)    
    recurse(p)

if N == visited.count(1):
    print(0)
else:
    print(N - visited.count(1) - root_number) # root의 개수 필요
