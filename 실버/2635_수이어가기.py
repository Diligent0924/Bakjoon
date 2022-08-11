# count로 하나씩 증가시키면서 뒤쪽에 두개 있는걸 뺀 차이만큼을 새로운 곳에 append함
# 
N = int(input())
count,result_1,result_2 = 0,0, []
while count < N:
    # count는 N까지 계속 추가해서 일일히 확인하는데 쓰인다.
    count += 1
    # list_a는 처음 시작할 때 쓰이며 해당 list가 아래에서 돌아가면서 계속 추가해주는 list
    list_a = [N, count]
    while True:
        # 제일 마지막 2개가 음수가 나오면 break를 걸어야 한다.
        if list_a[-2] - list_a[-1] < 0:
            # result_1은 가장 길었던 것의 개수이고 계속 갱신하는 것
            # result_2는 가장 길었던 것의 list형태를 묶어놓은 것
            if len(list_a) > result_1:
                result_1 = len(list_a)
                result_2 = list_a
            break
        else:
            # 마지막이 음수가 아니면 list_a에 계속 값을 더해준다
            list_a.append(list_a[-2] - list_a[-1])

print(result_1)
print(' '.join(map(str, result_2)))