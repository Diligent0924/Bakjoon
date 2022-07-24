# list 하나를 만든다. => 번호표 뽑은 사람은 그만큼 앞으로 보내고 그뒤로는 다시 세운다.
# len(list_a)-n을 통해서 확인이 가능하다. list를 쪼갤 때는 [a]와 같은 index는 허용되지 않는다?
# insert에 대한 생각 => 어떤 변수에 넣지 않고 바로 insert(index,값)으로 사용해야함
N = int(input())
list_a = list(map(int, input().split())) 
list_b = []
for i in range(N):
    list_b.insert(len(list_b)-list_a[i], i+1)

for i in list_b:
    print(i, end = ' ')