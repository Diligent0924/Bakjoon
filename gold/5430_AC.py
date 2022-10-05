from collections import deque
T = int(input())

for test_case in range(1,T+1):
    p = input()
    n = int(input())
    l = input()
    
    arr = deque()
    zero = False
    direction = True # popleft하게
    
    word = ''
    for i in range(len(l)):
        if l[i] not in ("[",",","]"):
            if l[i+1] == "," or l[i+1] == "]":
                word += l[i]
                arr.append(word)
                word = ''
            else:
                word += l[i]
    
    # print(arr)
    for i in p:
        if i == "R":
            direction = not direction
        elif i == "D":
            if not arr:
                zero = True
                break
            else:
                if direction:
                    arr.popleft()
                else:
                    arr.pop()
    
    if zero:
        print("error")
    else:
        if direction:
            print(f"[{','.join(arr)}]")
        else:
            print(f"[{','.join(list(arr)[::-1])}]")