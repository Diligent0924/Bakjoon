def solution():
    new_arr = []
    while list_a:
        temp = list_a.pop(0)
        new_arr.append(temp)
        if temp == '-':
            minus_arr = []
            while list_a:
                if list_a[0] == "-":
                    break

                number_1 = list_a.pop(0)
                if number_1 != "+":
                    minus_arr.append(int(number_1))
            new_arr.append(sum(minus_arr))
    # print(new_arr)
    count = 0
    while new_arr:
        a = new_arr.pop(0)
        if a == "-":
            b = new_arr.pop(0)
            count -= int(b)
        elif a == "+":
            b = new_arr.pop(0)
            count += int(b)
        else:
            count += int(a)
    return count



arr = list(input())
list_a = []
# 숫자와 연산자를 나누기 위한 방법
temp = []
for i in range(len(arr)):
    a = arr.pop(0)
    if a not in ("+", "-"):
        temp.append(a)
    else:
        list_a.append(str("".join(temp)))
        list_a.append(a)
        temp = []

list_a.append(str("".join(temp)))

print(solution())


