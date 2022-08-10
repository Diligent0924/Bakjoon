# 구조를 하나하나씩 차례대로 생각하면서 푸는게 훨씬 빨리 푸는 방법인것 같다.
# 주석 잘 달아줘야 내가 어떤 부분에서 틀렸는지 알기가 쉽다.
# 예외처리가 있다면 if문으로 먼저 처리하는 방법이 좋은 것 같다. (시간복잡도도 없음)

T = int(input())

for _ in range(T):
    # N : 문서의 개수 / M : 원하는 사람 => 위치가 어디인가?
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))
    arr_2 = [[i,v] for i,v in enumerate(arr)]
    result = []
    while True:
        # 항상 최댓값을 갱신
        max_a = arr_2[0][1]
        for i in range(len(arr_2)):
            if arr_2[i][1] > max_a:
                max_a = arr_2[i][1]
        #print(f'list : {arr_2} max_a : {max_a}')
        # arr 개수에 따른 변화값
        if len(arr_2) == 1: # arr_2가 하나밖에 없다면 무조건 1
            result.append(arr_2.pop(0))
            break
        else: # arr_2가 두개 이상이라면
            # 제일 앞에 있는게 max_a보다 작으면 뒤로 옮겨주기
            if arr_2[0][1] < max_a:
                s = arr_2.pop(0)
                arr_2.append(s)
            
            # max_a값이라면 M과 같은지를 확인하고 같다면 count를 print하기
            if arr_2[0][1] == max_a:
                if arr_2[0][0] == M:
                    result.append(arr_2.pop(0))
                    break
                else:
                    result.append(arr_2.pop(0))
    print(len(result))