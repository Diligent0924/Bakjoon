# deque에 대해서 배울 수 있었다.
# deque의 popleft(),appendleft()는 기존 list와는 다르게 빠르게 만든다.

from collections import deque
arr = deque([i for i in range(1,int(input())+1)])
count = len(arr) # 처음 arr의 개수를 확인한다.

if count == 1: # 예외처리 : count = 1이면 arr[1]이 없으므로 바로 답
    print(arr[0])
else:
    while len(arr) > 2: # 2번씩 반복하기 때문에 반드시 2개가 남으면 멈춰야한다.
        arr.popleft() # 오른쪽을 한번 빼준다.
        arr.append(arr.popleft()) # 오른쪽을 다시 가져다 끝에 둔다.

    print(arr[1]) # 2개가 남으면 두번째를 출력한다.