def subset(word):
    for i in range(len(word)-1): # 2중 for문으로 해야 전체를 확인할 수 있다.
        for j in range(1, len(word)):
            if word[i:j] == word[j:]:
                return False
    return True
    
def dfs(word):
    global min_count
    a = subset(word)
    if a == False:
        return
    
    if len(word) == N:
        print(word) # 여기부분에서 빨리 끝나면 바로 끝내야한다. => 안그러면 계속 뒤쪽이 돌아감
        quit()
    else:
        for i in ("1","2","3"):
            if word[-1] != i:
                dfs(word+i)

N = int(input())
for i in ("1","2","3"):
    dfs(i)