'''

'''

import sys
input = sys.stdin.readline
N = int(input())
arr = input()
if N % 2 == 1: # 만약 홀수라면 끝낸다.
    print(-1)
else:
    result = 0
    while arr: # arr가 있을 때까지 계속 진행한다.
        if arr == "((" or arr == "))":
            print(-1)
            exit()

        result += 1
        # print(arr)
        new_arr = ""
        middle = ""
        for i in arr:
            if not middle:
                middle += i
            else: # 만약 middle이 있다면
                if i == ")" and middle == "(" or i == "(" and middle == ")":
                    middle = ""
                else:
                    new_arr += middle
                    middle  = i
        arr = new_arr

    print(result)