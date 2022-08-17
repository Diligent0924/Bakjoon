'''
반갈이 기법에 대해서 다시 한번 알 수 있었다.
반갈이 기법은 정렬되어있는 수에서 어떤 특정한 수를 찾으려 할때 사용하는 수이다.
해당 문제는 h의 어느 지점에서 자르는지를 물어보았고 h의 최대값을 줬으므로 반갈이로 찾아내는 것이 빠르다.
최소/최대 ~~와 같은 방법도 어떤 특정값을 원하는 것이기 때문에 반갈이 기법 사용 가능하다.
=> 항상 반갈이 기법에 대하여 숙지하고 있는 것이 좋을 것 같다.

map,lambda기법에 대해서도 알 수 있었다. 
map(lambda x: (조건), list)와 같은 방식으로 사용한다.
해당 문제에서는 나무를 자른 윗퉁이 부분만을 남기도록 했다.
lambda에서도 if else 기법이 적용될 수 있었다.

'''

import sys
N, M = map(int, sys.stdin.readline().split()) # 나무의 수 / 가져가려는 나무 m
arr = list(map(int, sys.stdin.readline().split()))

start = 0 # 시작은 0부터 시작한다.
end = 1000000000 # h의 최대값
while start <= end: # 반갈이 기법을 사용한다.(반드시 start <= end여야 한다.)
    mid = (start+end) // 2
    list_a = list(map(lambda x: x - mid if x-mid > 0 else 0, arr)) # 윗퉁이 부분만 확인하는 것이므로 음수는 0으로 변경해준다.
    #print(start,end, mid, sum(list_a))
    sum_list_a = sum(list_a) # 나무 위쪽 부분의 합. 여러번 나오는 식은 변수로 한번 지정해야 메모리를 덜 먹는다.
    if sum_list_a < M:
        end = mid-1
    elif sum_list_a > M:
        start = mid+1
        result = mid # 핵심포인트!! M과 같지 않더라도 가장 가까운 수가 나와야 하므로 mid를 넣는다.
    else: # 만약에 M과 같이 나온다면 최적의 방법이므로 mid값이 나와야한다.
        result = mid
        break
print(result)