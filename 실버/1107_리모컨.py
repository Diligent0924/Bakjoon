N = input()
M = int(input())
lost_number = set(list(map(int, input().split())))
numbers = list(set([0,1,2,3,4,5,6,7,8,9]) - lost_number)

result = 0
count = 0

for i in range(len(N)):
    # 숫자를 하나하나씩 확인했을 때 값이 작은 것을 먼저 판별해야함
    number = int(N[i])
    if number in numbers: # 같은 숫자라면 한번만 누르면 됨
        count += 1