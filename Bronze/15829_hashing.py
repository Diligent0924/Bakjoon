'''
ord(문자) : 문자를 숫자로 치환해주는 방법
islower() : 해당 글자가 소문자인지 확인하는 방법

'''
N = int(input())
a = input()
result = 0
count = -1
for i in a:
    count += 1
    if i.islower() == True:
        result += (ord(i) - 96) * (31**(count))
    
print(result % 1234567891) # 대문자일때도 치환해주는 방법이라고한다...
