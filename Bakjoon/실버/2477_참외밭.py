melon = int(input())
index_a, list_b, dic = [], [], {1:[],2:[],3:[],4:[]}
for i in range(6):
    a, b = map(int, input().split())
    index_a.append(a)
    list_b.append(b)
    dic[a].append(b)
def solution(n):
    bat = [[1,1,2,3,3,4],[1,2,2,3,3,4],[1,2,2,3,4,4],[1,1,2,3,4,4]]
    result_bat = [[2,4,2],[4,4,1],[1,1,3],[3,2,3]]
    result = result_bat[bat.index(n)]
    a = list_b[(index_a.index(result[0]) + 2) % 6]
    b = list_b[(index_a.index(result[0]) + 3) % 6]
    width = dic[result[1]][0] * dic[result[2]][0]
    width -= b * a
    return width*melon
print(solution(sorted(index_a)))
# if index_b == [1,1,2,3,3,4]:
#     a = list_b[(index_a.index(2) + 2) % 6]
#     b = list_b[(index_a.index(2) + 3) % 6]
#     width = dic[4][0] * dic[2][0]
#     width -= b * a
#     print(width*melon)
# elif index_b == [1,2,2,3,3,4]:
#     a = list_b[(index_a.index(4)+2) % 6]
#     b = list_b[(index_a.index(4)+3) % 6]
#     width = dic[4][0] * dic[1][0]
#     width -= a * b
#     print(width*melon)
# elif index_b == [1,2,2,3,4,4]:
#     a = list_b[(index_a.index(1)+2) % 6]
#     b = list_b[(index_a.index(1)+3) % 6]
#     width = dic[1][0] * dic[3][0]
#     width -= a*b
#     print(width*melon)
# elif index_b == [1,1,2,3,4,4]:
#     a = list_b[(index_a.index(3)+2) % 6]
#     b = list_b[(index_a.index(3)+3) % 6]
#     width = dic[2][0] * dic[3][0]
#     width -= a * b
#     print(width*melon)

