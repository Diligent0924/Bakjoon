'''
어떤 도형이 지속적으로 반복되는 것을 알 수 있다. => DP 문제이다.
'''

DP = [1, 1, 1, 2, 2]

tc = int(input())
for _ in range(tc):
    N = int(input())
    if len(DP) > N+1:
        print(DP[N-1])
    else:
        while True:
            DP.append(DP[-1] + DP[-5])
            if len(DP) > N+1:
                print(DP[N-1])
                break