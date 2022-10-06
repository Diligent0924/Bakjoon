'''
돌릴 때마다 가능한 모든 경우의 수를 구한 뒤에 하나하나씩 제거해 나간다.
'''

from itertools import permutations
N = int(input())
all_list = list(permutations([1,2,3,4,5,6,7,8,9], 3))
result = [[] for _ in range(N+1)]
id = 0
for _ in range(N):
    id += 1
    number, strike, ball = map(int, input().split())
    number = str(number)
    num_1, num_2, num_3 = int(number[0]), int(number[1]), int(number[2])
    number_list = [num_1, num_2, num_3]
    if strike == 1:
        for i in number_list:
