'''
소수구하기는 특별한 방식으로 풀어야하는 것 같다.
수학적 방법으로 접근해야 되는데 무슨 소린지 솔직히 모르겠다.
나중에 그냥 한번 보면 될거같다.
'''


def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1): # 3이면 루트3??
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)