'''
어려웠던 부분 : 만약 ())일 경우의 예외처리가 부족했다.
stack을 사용하여 풀었으며 그냥 전체부분을 한 list에 넣어 풀었다.

일부 예외처리 부분에서 애를 먹었다. 이러한 부분을 꼼꼼히 봐야할거같다.

'''
import sys
while True:
    line = sys.stdin.readline()
    if line[0] == '.': # 그냥 line을 넣으면 끝나지가 않는다 왜?
        break
    list_a = [0] # 맨 처음에 ")","]"가 나오면 index_Error가 나오므로 padding한다.
    for i in line:
        if i == "(" or i == "[":
            list_a.append(i)

        elif i == ")":
            if list_a[-1] == "(": # 만약 짝이 있다면 pop해서 없애준다.
                list_a.pop()
            else:
                list_a.append(i) # ())일 경우 그냥 넘어가면 안되므로 추가해준다.
        elif i == "]":
            if list_a[-1] == "[":
                list_a.pop()
            else:
                list_a.append(i)
    
    if len(list_a) == 1: # list_a = [0]이면 전부다 짝이 있다.
        print('yes')
    else:
        print("no")
            