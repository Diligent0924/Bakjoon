# 변수를 direction인데 dirction으로 잘못 써서 엄청나게 해맸었음 => 정확하게 쓸 필요 있음
# 전체적인 큰 틀을 정해놓고 푸는 것이 중요함 => 방향을 기준으로 풀었음
# 완전탐색을 처음에 생각하고 풀어야함 => 특이한 경우를 하나씩 빼는것이 옳음
garo, sero = map(int, input().split())
N = int(input())

graph = [[0] * garo for _ in range(sero)]

a, b = 1, 0
count, size = 0, 0
k,direction = 0, 'up'

if garo * sero < N:
    print(0)
else:
    while count < N:
        count += 1
        #print(direction)
        
        if direction == "up":
            b += 1
            #print(count, a, b)
            if b == sero-k:
                direction = 'right'

        elif direction == 'right':
            a += 1
            if a == garo-k:
                direction = 'down'
            #print(count, a, b)
            
        elif direction == 'down':
            b -= 1
            if b == 1+k:
                direction = "left"
            #print(count, a, b)
        elif direction == 'left':
            a -= 1
            #print(count, a, b)
            if a == 1+k and b == 1+k:
                k += 1
                a = 1+k
                b = 1+k
                direction = 'up'
        if count == N:
            print(a, b)