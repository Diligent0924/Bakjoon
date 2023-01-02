from collections import defaultdict
N, K = map(int, input().split())
bottle = defaultdict(int)
bottle[1] = N
origin = N
liter, buy = 1, 0
while True:
    while bottle[liter] > 1:
        bottle[liter] %= 2 # 2번을 지운다.
        bottle[liter*2] += bottle[liter] // 2 # 한개를 채운다.
        liter *= 2
    
    
    # 만약 위에서 충족시키지 못했다면