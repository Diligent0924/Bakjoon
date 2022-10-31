'''
정규표현식에 대한 내용이다.
'''

import re

T = int(input())

for _ in range(T):
    pb = input()
    match = re.compile('(100+1+|01)+')
    result = match.fullmatch(pb) # compile을 기준으로 모든 문자열이 완벽하게 들어맞는지를 확인한다.

    if result:
        print("YES")
    else:
        print("NO")