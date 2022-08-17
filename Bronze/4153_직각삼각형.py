'''
while문에서 어떤 특정 case가 나올 때 break를 걸 수 있는지를 확인
예외처리에 대한 중요성에 대해서 다시 배울 수 있었다.
코드가 길어지는 것은 중요하지 않다.
'''
while True:
    list_a = list(map(int, input().split()))
    if list_a == [0,0,0]:
        break

    max_line = max(list_a)
    line_1,line_2 = 0,0
    for i in list_a:
        if i != max_line:
            line_1 += i**2
        else:
            line_2 += i**2

    if line_1 == line_2:
        print('right')
    else:
        print('wrong')