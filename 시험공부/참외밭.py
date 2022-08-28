'''
참외밭 면적 당 개수 : N
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

if arr[(max_i-1)%6] > arr[(max_i+1)%6]:
    max_side = arr[(max_i-1)%6]
    min_side = arr[(max_i+1)%6]
    min_side_i = (max_i+2)%6
else:
    min_side = arr[(max_i-1)%6]
    max_side = arr[(max_i+1)%6]
    min_side_i = (max_i-2)%6

print(((max_arr * max_side) - ((max_side - min_side) * arr[min_side_i])) * N)

