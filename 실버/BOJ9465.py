'''
점화식 방법은 맞았으나 index 부분에서 계속해서 에러가 뜬 것을 알 수 있었음.
기본적으로 DP 문제에서 바로 틀린 답이 나온다면 index 문제를 생각해야함
=> 내가 생각한 점화식이 거의 대부분 틀리게 나온다면 index 먼저 확인할것!(반드시)
처음 시작하는 값을 따로 지정하지 않고 안에 바로 넣는 것이 좋아보임  
'''
T = int(input())
for _ in range(T):
    N = int(input())
    stickers = [list(map(int,input().split())) for _ in range(2)] 
    # 여기서 바로 stickers로 들어가도 괜찮은 방법인거 같음
    if N == 1: # 만약 1개라면 그냥 둘 중에서 하나로 끝내면 된다
        print(max(stickers[0][0], stickers[1][0]))
    else: # 만약 2개가 넘는다면
        for i in range(1, N): 
            if i == 1: # i가 1일 경우에는 i-2가 음수가 나오므로 항상 대각선 방향으로 더하는 것이 가장 크다
                stickers[0][1] += stickers[1][0] 
                stickers[1][1] += stickers[0][0]
            else: # 2 이상일 경우에는 두가지 경우의 수로 생각되어지는데 1. 한칸을 아예 띄는 방식 2. 대각선 방식
                stickers[0][i] += max(stickers[1][i-1], stickers[1][i-2])
                stickers[1][i] += max(stickers[0][i-1], stickers[0][i-2])
        
        result = 0 
        for m in stickers: # 결과값을 확인하는 방식
            if max(m) > result:
                result = max(m)
        print(result)
            
            
    # # print(stickers)
    # if N == 1:
    #     print(max(stickers[0][0], stickers[1][0]))
    # elif N == 2:
    #     print(max(stickers[1][0] + stickers[0][1], stickers[0][0] + stickers[1][1]))
    # else: # N이 최소 3개 이상여야 사용가능하다.
    #     DP = [[0] * (N) for _ in range(2)]
    #     # 제일 앞에 뭐부터 시작할지를 확인하고 들어가야한다.
    #     DP[0][0],DP[1][0] = stickers[0][0],stickers[1][0]
    #     DP[0][1],DP[1][1] = DP[1][0] + stickers[0][1], DP[0][0] + stickers[1][1]   
    #     # 숫자가 커지는 방식으로 이용하면 될듯
    #     for i in range(2,N):
    #         DP[0][i] = max(DP[1][i-1], DP[1][i-2]) + stickers[0][i]
    #         DP[1][i] = max(DP[0][i-1], DP[0][i-2]) + stickers[1][i]
    #     # print(DP)
    #     print(max(DP[0][N-1], DP[1][N-1]))