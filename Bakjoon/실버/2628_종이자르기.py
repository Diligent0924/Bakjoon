# 가로와 세로 각각으로 판단한다.
# 가로면 [0:i], [i,j]형태로 만든다. 세로 또한 마찬가지이다.
# insert로 0을 넣어서 표시한다
# insert에 대하여 공부할 수 있었다.
garo, sero = map(int, input().split())
N = int(input())
garocut, serocut = [], []
for _ in range(N):
    a, b = map(int,input().split())
    if a == 0:
        serocut.append(b)
    else:
        garocut.append(b)

garo_result, sero_result = [], []
count = 0
for i in range(1,garo+1):
    count+= 1
    if i in garocut:
        garo_result.append(count)
        count = 0
garo_result.append(count)

count = 0
for i in range(1,sero+1):
    count+= 1
    if i in serocut:
        sero_result.append(count)
        count = 0
sero_result.append(count)

garo_result.sort()
sero_result.sort()
print(garo_result[-1] * sero_result[-1])

