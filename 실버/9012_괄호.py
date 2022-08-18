'''
개수를 세서 해도 상관은 없어보이나 stack이 더 직관적이라서 사용
"("는 무조건 더하고 만약 ")"일때 앞에 "("가 없다면 더해줌으로써 len(list) >1 으로 하는 방법
이후에 개수를 통한 방법에 대해 공부해야할거같음
'''
N = int(input())
for _ in range(N):
    a = input()
    list_a = []
    for i in a:
        if i == "(":
            list_a.append(i)
        
        if i == ")":
            if len(list_a) == 0 or list_a[-1] != "(":
                list_a.append(i)
            else:
                list_a.pop()
        
    if len(list_a) == 0:
        print("YES")
    else:
        print("NO")