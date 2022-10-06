<<<<<<< HEAD
pre_number = int(input())
N = list(map(int, str(pre_number))) # 원하는 수
M = int(input()) # 의미없음
if M != 0:
    arr = list(map(int, input().split()))
else:
    arr = []
number = list(set([0,1,2,3,4,5,6,7,8,9]) - set(arr))

if number == []:
    print(abs(pre_number-100))
    exit()

channel = 100 # 현재 채널
count = 0 # 몇번을 누르는가
push_channel_up = ''
push_channel_down = ''
# 각 숫자마다
for i in range(len(N)):
    count += 1
    if N[i] in number:
        push_channel_up += str(N[i])
        push_channel_down += str(N[i])
    else:
        min_x = 100
        min_j = ""
        for j in number:
            if abs(j-N[i]) < min_x and j-N[i] > 0:
                min_j = str(j)
                min_x = abs(j-N[i])
        push_channel_up += min_j

        min_x = 100
        min_j = ""
        for j in number:
            if abs(N[i]-j) < min_x and N[i]-j > 0:
                min_j = str(j)
                min_x = abs(N[i]-j)
        push_channel_down += min_j
        break

# 뒤쪽에는 최대한 높은 숫자가 보일 수 있도록 해준다.
a = (len(N) - len(push_channel_up))
b = (len(N) - len(push_channel_down))
push_channel_up = int(push_channel_up + (str(min(number)) * a))
push_channel_down = int(push_channel_down + (str(max(number)) * b))

# +, -로 이동하는 숫자를 추가한다.
count_1 = count + abs(pre_number - push_channel_up) + a
count_2 = count + abs(pre_number - push_channel_down) + b

# 100에서 이동하는 것과 비교해서 최소 count 값을 찾는다.
result = min(abs(100-pre_number), count_1, count_2)
# print(abs(100-pre_number), count_1, count_2)
print(result)
=======
def solution(now):
    global number, result
    for i in str(now):
        if i not in number:
            return
    # 만약 더 작으면
    if abs(N-result) > abs(N-now):
        result = now
        return
        
N = int(input())
M = int(input())
origin_number = set(["0","1","2","3","4","5",'6',"7","8","9"])
if not M:
    number = list(origin_number)
else:
    arr = set(input().split())
    number = list(origin_number - arr)

now = -1 # 현재 위치
result = -10000
while now < 1000000:
    now += 1
    solution(now)

# print(result)
count = 0
for i in str(result):
    count += 1

count += abs(N - result)
answer = min(count, abs(N-100))
print(answer)
>>>>>>> 9a846e67484bd15e912fbbf5a1eec9e67b86ef81
