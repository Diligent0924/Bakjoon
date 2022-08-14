'''
원형 큐에 대한 문제이다.
만약 K가 아니라면 append와 pop을 동시에 씀으로서 맨앞 => 맨뒤 형태로 넣는다.
while문으로 계속 돌아가기 때문에 가능하다.
'''
a, b = map(int, input().split())
arr = [i for i in range(1,a+1)]
K = b
arr_2 = []
count = 0
while len(arr) != 0:
    count += 1
    if count == K:
        arr_2.append(arr.pop(0))
        count = 0
    else:
        arr.append(arr.pop(0))

print(f'<{", ".join(map(str,arr_2))}>')