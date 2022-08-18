import sys
N, K = map(int, sys.stdin.readline().split())
list_a = [int(sys.stdin.readline()) for _ in range(N)]
def solution(list_a,start, end,K):
    # print(start,end)
    if start+1 >= end:
        if sum(list(map(lambda x: x//start, list_a))) != sum(list(map(lambda x: x//end, list_a))):
            return start
        else:
            return end
    # if start > end:
    #     return end
    a = (start + end) // 2
    result = list(map(lambda x: x//a, list_a))
    if sum(result) < K:
        return solution(list_a, start, a,K)
    elif sum(result) >= K:
        return solution(list_a, a, end,K)

if K==1:
    print(max(list_a))
else:
    a = solution(list_a, 1, max(list_a),K)
    print(a)