'''
combinations를 이용해 이항계수를 센다!
'''

from itertools import combinations
a, b = map(int, input().split())
list_a = [i for i in range(a)]
print(len(list(combinations(list_a,b))))