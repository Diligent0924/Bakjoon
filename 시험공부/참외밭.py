'''
참외밭 면적 당 개수 : N
주어진 조건 arr에 2배를 곱하고 가장 큰값 찾기
가장 큰값 양옆 확인 => 가장 큰값 * 옆에서 가장 큰값(전체 면적)
양 옆 (큰값 - 작은값) * (작은 옆값의 옆)
'''

N = int(input())
arr = []
for _ in range(6):
    a, b = map(int, input().split())
    arr.append(b)

max_arr = 0
max_i = -1
for i in range(6):
    if arr[i] > max_arr:
        max_i = i
        max_arr = arr[i]

# 양 옆중에 더 큰값 찾기
if max_i - 1 < 0:
    a = arr[-1]
else:
    a = max_i - 1

if max_i + 1 >
max_side = max(arr[a], arr[max_i+1])

print(-1%3)
