'''
진실을 아는 사람의 번호가 나오는 경우 => 진실을 이야기해야함 (들은 모든 사람은 진실 list에 들어가야함)
진실을 아는 사람이 아무도 없는 경우 => 거짓을 말한다. (들은 사람 모두 거짓을 항상 들어야함) 
'''
N, M = map(int, input().split())
real_list = list(map(int, input().split()))
parties = []
for _ in range(M):
    a = list(map(int, input()))
    a.pop(0)
    parties.append(a)
    