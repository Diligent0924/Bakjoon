'''
호텔을 세로로 올렸을 때 어떻게 활용할 것인가에 대한 문제였다.
예외처리 : 만약 나눈 나머지가 0이면 꼭대기 층이기 때문에 따로 관리해야한다.
붙여넣기를 했다가 이상한 부분에서 막혀서 시간을 잡아먹었다.
이러한 문제를 풀 때는 좀 더 확실하게 생각하고 풀어야한다.
또한 스스로 알고리즘이 거의 맞았다고 느낀다면 코드안에 사소한 것 떔에 틀릴 가능성이 높다.
'''


T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    
    if N%H == 0:
        first = str(H)
        if N//H >= 10:
            second = str(N//H)
        else:
            second = str("0") + str(N // H)        
    else:    
        first = str(N % H)
        if N//H + 1 >= 10:
            second = str(N // H + 1)
        else:
            second = str("0") + str(N // H + 1)
    print(int(first + second))