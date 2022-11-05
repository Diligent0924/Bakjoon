'''
최소 1개의 모음(aeiou)와 두 개의 자음(나머지) 이상 => 글자가 3개 이상
자음과 모음 list를 따로 나눠둔 후에 각각을 매칭하면 될 듯!
'''
from copy import deepcopy
def subset(arr,size,result):
    N = len(arr)
    for i in range(1<<N):
        temp = []
        for j in range(N):
            if i & (1<<j):
                temp.append(arr[j])
        if len(temp) >= size:
            result.append(temp)

L, C = map(int, input().split())
arr = list(input().split())

a_list = []
b_list = []
for i in arr:
    if i in ('a','e','i','o','u'):
        a_list.append(i)
    else:
        b_list.append(i)

a_sub = []
b_sub = []
subset(a_list,1,a_sub)
subset(b_list,2,b_sub)

result = []
for i in a_sub:
    word = ''
    # 해당 값 안에 있는 모든 값을 더한다.
    for h in i:
        word += h
    # 다 더했으면 다른 얘들도 해보자
    for j in b_sub:
        new_word = deepcopy(word)
        for n in j:
            new_word += n
        new_word = sorted(new_word)
        s = ''
        for l in new_word:
            s += l
        if s not in result and len(s) == L:
            result.append(s)
# print(result)
result.sort()
for i in result:
    print(i)