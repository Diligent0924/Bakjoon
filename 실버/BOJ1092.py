'''
박스를 크레인에 넣는다는 생각만 하다보니까 시야가 너무 좁아졌다
어떤 문제든 반대의 경우에도 생각을 하는 것이 좋을 것 같다.

이 문제에서 작은 것부터 시작하는 것과 큰 것부터 시작하는 것과의 차이가 있는데 어떤 경우에 그러는지 모르겠다.
특정한 경우에는 답이 달라진다. (최대값이 많은 경우...)
=> 만약 알고리즘이 틀리지 않았다고 생각한다면 반대의 경우를 확인하는 것도 좋은 방법이라고 생각한다.
'''

from copy import deepcopy
import sys
input = sys.stdin.readline
N = int(input())
# 왜 큰거부터 넣어야 하는지 이유를 도저히 모르겠다.
cranes = sorted(list(map(int, input().split())), reverse= True)
M = int(input())
boxes = sorted(list(map(int, input().split())), reverse= True)
if boxes[0] > cranes[0]: # 만약 박스를 옮길 수 없을 때 : 크레인의 최대 무게량보다 무거운 짐이 있는 경우
    print(-1)
else:
    # time = 0

    # while boxes:
    #     if not boxes:
    #         break

    #     for crane in cranes:
    #         for box in boxes:
    #             if crane >= box:
    #                 boxes.remove(box)
    #                 break

    #     time += 1

    # print(time)
    count = 0
    while boxes: # 필요한 박스가 있을 때만 지속한다.
        # print(boxes)
        count += 1 # 한번 들 때마다 하나씩 추가한다.
        remove_list = []
        real_crains = deepcopy(cranes)
        for box in boxes: # 박스를 하나하나씩 확인한다.
            for crain in real_crains: # 크레인도 하나하나씩 확인한다.
                if crain >= box:
                    remove_list.append(box)
                    real_crains.remove(crain)
                    break
        for r in remove_list:
            boxes.remove(r)
    
    print(count)