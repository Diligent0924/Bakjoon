'''
짝수일 때 => 무조건 전체가 짝수여야 한다.
홀수일 때 => 짝수 + 어느 한개만 홀수여야한다.
'''
word = list(input())
word.sort()
dic = {}
# dic[i] = dic.get(i,0)+1
for i in word:
    dic[i] = dic.get(i,0) + 1

if not len(word) % 2: # 짝수일 때 사용
    # 짝수일 때 홀수가 있으면 안됨
    for i in dic:
        if dic[i] % 2:
            print("I'm Sorry Hansoo")
            break
    else: # 전부 짝수라면 반만큼만!!
        result = ''
        for i in dic:
            result += i * (dic[i]//2)

        for i in range(len(result)-1,-1,-1):
            result += result[i]
        print(result)
else: # 홀수
    # 홀수가 한개라면 괜찮지만 만약 여러개라면 팰린드롬이 성립하지 않음.
    holsu = 0
    holsu_value = ''
    for i in dic:
        if dic[i] % 2:
            holsu += 1
            holsu_value += i
        if holsu == 2:
            print("I'm Sorry Hansoo")
            break
    else:
        result = ''
        for i in dic:
            result += i * (dic[i]//2)
        result += holsu_value
        for i in range(len(result)-2,-1,-1):
            result += result[i]
        print(result)