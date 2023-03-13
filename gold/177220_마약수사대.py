'''
문제점
  - 문제에 대한 해석에 대한 에러가 있었다.
  - 나의 경우 부모 및 자식 노드를 모두 버리게끔 사용했으나 자식기준에서 부모가 2명이라면 마약이 공급된다는 것을 간과함
  - 먀약 공급원은 결국 root 마약에게 약을 받아야한다는 개념을 알아야함

풀이방법
  - root 마약원을 확인함 => 자식 기준에서 Dictionary를 통하여 없다면 root 마약원임
  - 검거된 노드들의 간선을 모두 제거해야함 (만약 검거된 노드만 부모 노드인 자식 노드들은 기존 root와는 따로 떨어짐)
  - root에서부터 시작하여 연결된 노드들의 개수를 확인함
  
소감
  - 그래프의 경우 어떤 부분이든 연결이 된다는 것을 생각하고 문제를 풀어야 한다.
  - 하나의 기준이 아닌 반대쪽 기준에서도 확인을 해야 한다.
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
            # print(node)
            for h in arr[node]: # 갈 수 있는 곳을 한번씩 확인한다.    
                if not visited[h]: 
                    visited[h] = 1
                    remain.add(h)
                    queue.append(h)

print(len(remain))