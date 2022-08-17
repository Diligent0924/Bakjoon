list_a = []

def push_front(X):
    return list_a.insert(0,X)

def push_back(X):
    return list_a.append(X)

def pop_front(list_a):
    if len_a == 0:
        return -1
    else:
        return list_a.pop(0)

def pop_back(list_a):
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
def front(list_a):
    if len_a == 0:
        return -1
    else:
        return list_a[0]
    
def back(list_a):
    if len_a == 0:
        return -1
    else:
        return list_a[-1]

import sys
N = int(sys.stdin.readline())
for _ in range(N):
    a = sys.stdin.readline()
    len_a = len(list_a)
    if "push_front" in a:
        push_front(int(a[11:]))
    elif "push_back" in a:
        push_back(int(a[10:]))
    elif "pop_front" in a:
        print(pop_front(list_a))
    elif "pop_back" in a:
        print(pop_back(list_a))
    elif "size" in a:
        print(size(list_a))
    elif "empty" in a:
        print(empty(list_a))
    elif "front" in a:
        print(front(list_a))
    elif "back" in a:
        print(back(list_a))