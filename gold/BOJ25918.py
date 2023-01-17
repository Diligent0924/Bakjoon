'''
알고리즘 : 한번 돌고 한번 도는 방식으로 () )( 일때를 확인하는 것

예외처리 : 홀수는 무조건 -1이고 짝수의 경우 "((" "))"의 경우에는 -1이다

최적화 : while 문으로 계속 time에 따라 돌리는 것은 시간초과가 나므로 한번에 구하는 방식을 알아야 한다.

solution
만약 "(())" 이라고 할 때 하나씩 꺼내면 ( , (( , (() 방식으로 나타나므로 순간의 개수를 구하면 된다.
'''

N = int(input())
arr = input()

result = []
final = 0
for i in arr:
    if not result:
        result.append(i)
    else:
        a = result.pop()
        if a == "(" and i == ")" or a == ")" and i == "(":
            continue
        else:
            result.append(a)
            result.append(i)
    final = max(final, len(result))  # 해당 result의 개수에 따라 final 수가 바뀌는 것이 인상적

if result:
    print(-1)
else:
    print(final)