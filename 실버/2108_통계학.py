# sys.stdin.readline()에 대해서 배울 수있었다.
# 앞으로 시간초과가 난다면 무조건 readline으로 해보는 것이 바람직하겠다.
# Counting 정렬에서 배운것처럼 index와 count 수를 list로 만들어 준뒤 사용했다.
# -4000 ~ 4000까지여서 index를 생각하는데 오랜 시간이 걸렸다.
# 위와 같은 경우에는 0의 기준을 어디다 둘 것인지에 대해서 기준점을 잡고 풀어야겠다.

import sys
N = int(sys.stdin.readline())

arr = [0] * 8001
count,sum_a = 0, 0
medium_a = 0

for _ in range(N):
    a = int(int(sys.stdin.readline()))
    arr[a+4000] += 1
    # 산술평균에 필요한 것들
    sum_a += a
    count += 1 # len함수
          
# 산술평균
print(round(sum_a/count))

# 중앙값 : 가운데 값 N//2
medium_count = 0
for i in range(8002):
    medium_count += arr[i]
    if medium_count > N//2:
        print(i-4000)
        break

# 최빈값
count_max_a,c = 0, 0
max_arr = max(arr)
for i in range(8001):
    # count의 최대값을 찾아서 index를 확인
    if arr[i] == max_arr:
        c += 1
        count_max_a = i
    if c == 2:
        count_max_a = i
        break
print(count_max_a-4000)

# 최소값과 최대값
max_a, min_a = -4001,4001
for i in range(8001):
    if arr[i] > 0:
        min_a = i
        break
for j in range(8000,-1,-1):
    if arr[j] > 0:
        max_a = j
        break
print(max_a-min_a)