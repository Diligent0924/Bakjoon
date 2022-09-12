'''
크기를 기준으로 정렬한 뒤에 만약 해당 크기 내에 더 작은 크기가 있다면 대체해버리면 된다.
문제를 정확하게 읽는 능력이 있어야 할 것 같다. => 문제를 제대로 읽지 않아서 생긴 오류시간이 더 많은것 같다.
알고리즘을 짤 때 좀 더 정확하게 보는 방식이 중요하다.
'''
# def solution():
#     result = []
#     while list_a:
#         a, b = list_a.pop(0)
#         if not result:
#             result.append((a, b))
#         else:
#             c, d = result.pop()
#             if a >= d:
#                 result.append((c, d))
#                 result.append((a, b))
#             elif a >= c and b <= d:
#                 result.append((a, b))
#             else:
#                 result.append((c, d))
#     # print(result)
#     return len(result)
#
#
# N = int(input())
# count = 0
# list_a = []
# for _ in range(N):
#     a, b = map(int, input().split())
#     list_a.append((a, b))
#
# list_a.sort(key=lambda x: (x[0], (x[1] - x[0])))
# # print(list_a)
# print(solution())


#2번째 문제풀이
# 최대 회의 갯수 찾기
# 회의 시작시간이 겹치는 것은 전부 제일 작은걸로 갱신, (제일 작은 값으로 하니까 어떤 경우에 대하여 카운트를 못하는 경우가 발생하여 그냥 저장하는 방식으로 했음)
# 시작시간 키값, 도착시간 밸류로 딕셔너리에 저장할 것임
# 회의 시작 시간 순으로 정렬하여 출력 (keys 만 sort 하여 dic[key] 방식으로 불러올 것임)
# 현재 회의의 종료시간 저장 그리고 종료시간보다 늦은 시작 시간인 녀석이 나오면 종료시간 갱신 및 카운트 더하기 일
# 종료시간보다 종료시간이 더 이른 녀석이 나오면 종료시간 갱신, 카운트는 유지
import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    dic = {}
    # dic[start] = [end1..] 방식으로 dic 구성
    for _ in range(N):
        start, end = map(int, input().split())
        if dic.get(start):
            dic[start].append(end)  # min(dic.get(start, float('inf')), end)
        else:
            dic[start] = [end]

    for k in dic.keys(): # end value값이 작은 것부터 시작하기 위해서 사용
        dic[k].sort()

    keys = sorted(dic.keys()) # key값을 정렬해서 순서대로 넣어준다.
    end = 0
    count = 0
    print(dic)
    for key in keys:
        print(f'key : {key}, count : {count}, end : {end}')
        for e in dic[key]:
            if e < end: # 같은 범위 내에서 가장 작은 값을 찾는다.
                end = e
            elif key >= end: # 만약 start가 end보다 뒤에 있다면 해당 부분은 겹치는 부분이 없으므로 그냥 더해주면 된다.
                count += 1
                end = e # 해당 key값의 가장 긴 부분을 가져온다. => 이후에 계속 줄여나가면 된다.

    print(count)


solve()
