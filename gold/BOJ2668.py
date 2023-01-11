'''
순환 문제라는 것을 빠르게 캐치하면 풀기가 훨씬 수월할 것 같다.
A => B => A가 있어야 하기 때문에 순환! 이다!
문제가 각각의 순환되는 값을 찾는 것이다. => 이걸 간과했다.
'''
# def solution(arr_1,arr_2, now): # arr_1 : 1번째 리스트 / arr_2 : 2번째 리스트 / now : 현재 위치
#     global count, result
#     # 리스트가 같은지를 확인하기 위한 sort 함수
#     arr_1.sort()
#     arr_2.sort()
#     if arr_1 == arr_2 and len(arr_1) > count:
#         result = arr_1
#         return
#     else:
#         after = node[now]
#         if not visited[after]:
#             visited[after] = 1
#             arr_1.append(after)
#             arr_2.append(node[after])
#             solution(arr_1, arr_2, after)
#     return []
    

# N = int(input())
# node = [0] + [int(input()) for _ in range(N)] # node 값을 넣는다!
# same = []
# final = []
# for i in range(1, N+1):
#     if i == node[i]:
#         same.append(i)

# for i in range(1,N+1):
#     if i in same: # 자기 자신만 돈다면...
#         continue
#     count = 0 # arr_1의 최대 길이를 구해야하므로 저장한다.
#     result = []
#     visited = [0] * (N+1) # 해당 지역을 방문했는지를 확인한다.
#     visited[i] = 1 # 현재는 이미 있는 것이라고 생각한다.
#     arr_1, arr_2 = [], [] # 첫번째 리스트와 두번째 리스트를 빈칸으로 둔다.
#     arr_1.append(i)
#     arr_2.append(node[i])
#     solution(arr_1, arr_2, i)
#     if result:
#         for s in same:
#             if s not in result:
#                 result.extend(same)
    
#     if len(result) > len(final):
#         final = result

# print(len(final))
# for i in final:
#     print(i)
    

n=int(input())
arr=[0]*(n+1)
for i in range(1, n+1):
  arr[i]=int(input())

def dfs(x):
  global result
  visited[x]=True
  route.append(x)
  n=arr[x]
  if visited[n]:
    if n in route:
      result+=route[route.index(n):]
    return
  dfs(n)

result=[]
visited=[True]+[False]*(n+1)
for i in range(1, n+1):
  if not visited[i]:
    route=[]
    dfs(i)

result.sort()
print(len(result))
print(*result, sep='\n')