# 어떠한 list에서 특정 부분을 찾고자 할 때에는 반갈이 알고리즘이 가장 빠르다. (정렬 개념과 비슷하기 때문에)
# 반갈이 알고리즘은 end부분은 a-1, start부분은 a+1로 하면서 start > end 일때를 기본으로 한다.
# 단, 해당 특정 수에서 계속 진행하고 싶다면 특정 조건들을 잘 파악한 후에 사용하는 것이 중요하다. 

import sys
N, K = map(int, sys.stdin.readline().split())
list_a = [int(sys.stdin.readline()) for _ in range(N)]
def solution(list_a,start, end,K):
    # print(start,end)
    if start > end:
        return end
    a = (start + end) // 2 # 정수부분만을 탐색하기 때문에..
    result = list(map(lambda x: x//a, list_a))
    if sum(result) < K:
        return solution(list_a, start, a-1,K)
    elif sum(result) >= K:
        return solution(list_a, a+1, end,K)

if K==1:
    print(max(list_a))
else:
    a = solution(list_a, 1, max(list_a),K)
    print(a)
    
# 2번째 방법 : 1, a로만 판단했을 경우
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