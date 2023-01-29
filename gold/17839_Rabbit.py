def solution():
    visited = []
    visited.append("Baba")
    while visited:
        a = visited.pop()
        b = dic.get(a)
        if b:
            for value in b:
                if value not in result: # 이 부분 추가해야된다
                    result.add(value)
                    visited.append(value)

import sys
input = sys.stdin.readline
N = int(input())
result = set()
dic = {}
for _ in range(N):
    a, c = input().strip().split(" is ")
    if a not in dic:
        dic[a] = set([c])
    else:
        dic[a].add(c)

if "Baba" in dic:
    solution()

   
    for i in sorted(result):
        print(i)