'''
문자열의 모든 경우의 수를 확인해본다. => set나 dic을 사용하면 훨씬 빨라진다는 것을 기억하자...
'''
def backtracking(root,word):
    if root == 2 and word[0] == word[1]:
        return
    if root == N and word[-1] == word[-2]:
        return
    if 3 <= root < N and word[root-2] == word[root-1]:
        return
    if root == N:
        # print(word)
        dic_a.add(word)
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                backtracking(root+1, word+S[i])
                visited[i] = 0


S = list(input())
N = len(S)
visited = [0] * N
dic_a = set()
if len(S) == 1:
    print(1)
else:
    backtracking(0,'')
    print(len(dic_a))