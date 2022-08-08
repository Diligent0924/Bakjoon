# 하나씩 증가하면서 확인하는 방법
# 특정 문제에서 보이는 방법으로 일일히 확인하는 방법을 의미한다.
number = int(input())
a=0
while a<number:
    a += 1
    result = a
    for i in str(a):
        result += int(i)
    if result == number:
        print(a)
        break
    elif a==number:
        print(0)