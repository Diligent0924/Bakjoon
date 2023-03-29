'''
기본 조건 : 키 순서대로 sort, K개로 나눔
조건 1: 각 조에는 원생 1명 이상
조건 2: 같은 조 원생들은 서로 인접
최종 결과 : 비용이 최소가 되는 구간을 잡아라

Greedy 방식으로 사용 => 숫자 구간이 큰 순서대로 찾아서 하나씩 넣는 방식
크게 오르는 구간에 플래그를 넣는 것이 가장 효율적이다.

후기
1. 실제 조건을 확인해가면서 생각하는 것이 도움이 된다.
2. 들어가기 전 문제의 실체를 먼저 파악한 후에 들어가는 것이 옳다.
   => 미리 과정을 머리 속에 그려보면서 들어가야 한다는 의미이다.

'''
import heapq

N, K = map(int, input().split()) # N : 인원 수, K : 나눌 수 있는 수
arr = list(map(int, input().split()))
if K == 1:
    print(arr[N-1] - arr[0])
elif N == 1:
    print(arr[0])
else:
    distance = []
    heapq.heapify(distance)
    for i in range(N-1):
        heapq.heappush(distance, (-(arr[i+1] - arr[i]),i))
    s_index = []
    while K != 1:
        # 최대값을 하나씩 빼낸다.
        v, ind = heapq.heappop(distance)
        # 해당 위치에 플래그 값을 넣는다.
        s_index.append(ind+1)
        K -= 1
    s_index.sort() # 오름차순으로 만든다.
    start = 0
    result = 0
    # print(s_index)
    for i in s_index:
        # print(i-1,start)
        result += arr[i-1] - arr[start]
        start = i
    # print(arr)
    result += arr[N-1] - arr[start]
    print(result)