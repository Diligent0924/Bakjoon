a, b = map(int, input().split())
max_a = max(a,b)
number = 1
cheso = 1
while number < max_a:
    number += 1
    if a % number == 0 and b % number == 0:
        cheso *= number
        a = int(a / number)
        b = int(b / number)
        number = 1 # 2 나누고 그 뒤에 2일 때도 있으므로 number를 초기화해줘야한다.

chede = cheso * a * b
print(cheso)
print(chede)