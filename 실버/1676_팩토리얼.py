N = int(input())
answer = 1
for i in range(1,N+1):
    answer *= i
count = 0
for i in str(answer)[::-1]:
    if i == '0':
        count += 1
    else:
        break
print(count)