'''
sys의 위대함을 다시 한번 깨달을 수 있었다.
pop / push 등 stack의 함수를 만들어 볼 수 있어 좋았다.
'''

list_a = []

def push(X):
    return list_a.append(X)

def pop(list_a):
    if len_a == 0:
        return -1
    else:
        return list_a.pop()

def size(list_a):
    return len_a

def empty(list_a):
    if len_a == 0:
        return 1
    else:
        return 0
def top(list_a):
    if len_a == 0:
        return -1
    else:
        return list_a[-1]

import sys
N = int(sys.stdin.readline())
for _ in range(N):
    a = sys.stdin.readline()
    len_a = len(list_a)
    if "push" in a:
        push(int(a[5:]))
    elif "pop" in a:
        print(pop(list_a))
    elif "size" in a:
        print(size(list_a))
    elif "empty" in a:
        print(empty(list_a))
    elif "top" in a:
        print(top(list_a))