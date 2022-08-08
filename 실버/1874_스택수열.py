# 1~n까지 숫자가 무작위로 나열되어 있는 형태의 문제임
# 뒤에서부터 봤을때 앞에 자기보다 큰수 / 자기보다 작은 수가있다면 무조건 불가능
# 그렇기 때문에 숫자의 정렬은 다르더라도 위의 규칙을 항상 지켜야하기에 아래의 코드가 나온다.

# 해당 문제는 규칙을 좀 더 빠르게 찾으면 좋았을거 같다.
# 어떤 것을 기준으로 할 때 어떻게 나아가겠다는 방법을 좀 더 빠르게 캐치해야할거같다.
N = int(input())

list_a = [int(input()) for _ in range(N)]
list_b = []
result = []
for i in range(1,N+1):
    list_b.append(i)
    # print(list_a,list_b)
    result.append("+")
    while True:
        if len(list_a) == 0 or len(list_b) == 0:
            break
        elif list_b[-1] == list_a[0]:
            result.append("-")
            list_b.pop()
            list_a.pop(0)
            # print(list_a,list_b)
        # elif list_b[-1] > list_a[0]:
        #     if list_a[0] in list_b:
        #         list_b.pop()
        #         list_a.pop(0)
        #     else:
        #         print("NO")
        else:
            break

if len(list_a) > 0:
    print("NO")
else:
    for i in result:
        print(i)