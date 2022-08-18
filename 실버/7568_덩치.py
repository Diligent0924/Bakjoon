'''
Rank를 반대로 할 생각을 하지 못했다.
순서를 구할때 1,2,3으로 등수를 매겨야하므로 뒤에서부터 생각해야한다.
무의식적으로 앞에서부터 생각을 하니 이후 변경하기가 너무 어려웠다.

어떤 문제를 풀 때 다양한 관점에서 확인을 해야한다.
'''
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = [0] * N # Index와 Ranking을 연결하기 위하여 사용
for i in range(len(arr)):
    count = 0 # 기본적으로 자신보다 위는 없다는 것으로 초기화한것
    for j in range(len(arr)):
        '''
         이 부분에서 오래걸렸다. 계속 큰쪽으로만 count하려하니
         Error가 계속 발생했다. 뒤에서부터 count하면 빠른데
         생각이 고정되어 확인할 수 없었다.
        '''
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]: 
            count += 1
    result[i] += count + 1

print(*result)
    