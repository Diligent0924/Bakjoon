import sys
N, K = map(int, sys.stdin.readline().split())
list_a = [int(sys.stdin.readline()) for _ in range(N)]
def solution(list_a,start, end,K):
    print(list_a)
    if max(list_a) % 2 == 0 and start+1 >= end: # 이부분만 정리하면 될거 같다.
        return start
    elif max(list_a) % 2 == 1 and start >= end:
        return start
    a = (start + end) // 2
#    print(a)
    result = list(map(lambda x: x//a, list_a))
#    print(result)
    if sum(result) < K:
#        print(f'<K, {list_a} {start} {a}')
        return solution(list_a, start, a,K)
    elif sum(result) >= K:
        return solution(list_a, a, end,K)
    
a = solution(list_a, 0, max(list_a),K)
print(a)
# for i in range(a,b):
#     result = list(map(lambda x: x//i, list_a))
#     if sum(result) < K:
#         print(i-1)
#         break 
    
# 1번째 방법 : 1에서부터 시작해서 하나하나씩 확인해보는 방법 => 틀림
# N, K = map(int, input().split())
# list_a = [int(input()) for _ in range(N)]
# a = 0
# while True:
#     a += 1
#     result = map(lambda x: x//a, list_a)
#     if sum(result) < K:
#         print(a-1)
#         break