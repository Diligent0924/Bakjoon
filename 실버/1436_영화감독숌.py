# find 함수에 대해서 다시 한번 알게 되었다.
# find 함수 => str().find('000')으로 사용하며 특정 값이 있으면 제일 앞쪽 index를 가져오고 없다면 -1을 들고온다.

N, a, count = int(input()),0, 0 
while True:
    a += 1
    if str(a).find("666") != -1:
        count += 1
    
    if count == N:
        print(a)
        break