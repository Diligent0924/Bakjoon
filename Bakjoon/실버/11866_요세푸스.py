# 해당 인원을 제거한다.
# 한바퀴 돌때까지 list_a는 유지되야한다. 
# 한바퀴가 다 돌면 list_a에서 list_b를 뺴야한다. (list_b는 뺴야되는 수)
# 제거한 후의 list를 붙여넣는다.
from collections import deque

class Queue(deque):
    def enqueue(self,x):
        super().append(x)
    def dequeue(self):
        super().popleft()

    def display(self):
        for node in self.__iter__():
            print(node)