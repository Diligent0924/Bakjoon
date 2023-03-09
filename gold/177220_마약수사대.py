'''
단방향으로 확인이 가능하다.
A, B, C, D를 각각 0, 1과 같이 순서대로 넣는다. ord("A") - 65 방식을 사용
1. Root 
'''
from collections import defaultdict
def ord_change(alpha):
    return ord(alpha) - 65


N, M = map(int, input().split())
arr = [[] for _ in range(26)]
child_dic = defaultdict()
nodes = set()
root = []
for _ in range(M):
    a, b = map(str, input().split())
    arr[ord_change(a)].append(ord_change(b))
    nodes.add(ord_change(a))
    nodes.add(ord_change(b))
    if b not in child_dic:
        child_dic[ord_change(b)] = [ord_change(a)]
    else:
        child_dic[ord_change(b)].append(ord_change(a)) # 자식 기준으로 부모가 있는지를 확인한다.

police = list(input().split())[1:]
police = [ord_change(i) for i in police]

# 전체를 확인하면서 부모가 있는지 없는지를 확인한다.
for i in nodes:
    if i not in child_dic:
        root.append(i)

# 검거된 노드는 그냥 전체에서 삭제한다.
for i in police:
    for j in arr:
        if i in j:
            j.remove(i)

# print(root)
# print(police)
# print(arr)
remain = set()
visited = [0] * 26
for i in root:
    if i not in police:
        queue = [i]
        visited[i] =1
        while queue:
            node = queue.pop(0)
            print(node)
            for h in arr[node]: # 갈 수 있는 곳을 한번씩 확인한다.    
                if not visited[h]: 
                    visited[h] = 1
                    remain.add(h)
                    queue.append(h)

print(len(remain))