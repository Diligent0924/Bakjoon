'''
list_a라는 count 수를 저장하는 list를 가진다.
list_b는 +1/나누기 2 / 나누기 3에서 최소값을 찾기 위한 list를 가진다.
최솟값인것을 list_a에 추가한다.

DP 문제로 다운탑(작은수 => 큰수)로 가는 문제라고 한다.
이전 count를 추가한다는 생각을 못했다.
어떤 반복적인 부분이 있다고 생각되면 일단 해당 list 중 일부를 직접 찾아내서 확인해본다.
'''
a = int(input())
list_a = [0,0]
for i in range(2,a+1):
    list_b = []
    if i % 2 == 0:
        list_b.append(list_a[i//2] + 1)
    
    if i % 3 == 0:
        list_b.append(list_a[i//3] + 1)
    
    list_b.append(list_a[-1] + 1)
    
    min_a = min(list_b)
    
    list_a.append(min_a)

print(list_a[-1])