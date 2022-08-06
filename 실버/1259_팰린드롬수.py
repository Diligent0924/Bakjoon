# 펠린드롬 수에서 While문을 반드시 사용하게 하는 문제임
while True:
    a = input()
    if a == "0":
        break
    else:
        if a == a[::-1]:
            print('yes')
        else:
            print('no')