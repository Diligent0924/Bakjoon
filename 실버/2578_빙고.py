# 변수의 위치를 어디다 지정해야 가장 좋은지 확인할것!
# 분명 맞았는데 헷갈린다면 처음부터 하나하나씩 다 훑어보면서 공부하기!
# 구조 자체는 잘 짜놨는데 변수 하나 때문에 엄청나게 고생했다...
# 머리 속으로 for문 잘 돌려보기
bingopan = [list(map(int, input().split())) for _ in range(5)]
sahuaga = []
for _ in range(5):
    sahuaga.extend(list(map(int, input().split())))
M,N = 0,0 # 대각선에 쓰이는 방법
bingo_correct = [] # 기존에 들어있는 행인지 확인
bingo_correct_T = [] #기존에 들어있는 열인지 확인
number = 0 # 개수 세기
for i in sahuaga:
    count = 0 # 빙고가 얼마나 되었는지 확인
    number += 1
    # 사회자가 부른 것을 빙고판 안에서 찾아서 0으로 치환
    for j in range(5):
        for h in range(5):
            if bingopan[j][h] == i:
                bingopan[j][h] = 0
    # 치환한 후에 0이 행에 있는지 확인
    for j in bingopan:
        if sum(j) == 0:
            count += 1

    # 열에 전체 0이 있는지를 확인
    bingopan_T = list(map(list, zip(*bingopan)))
    for j in bingopan_T:
        if sum(j) == 0:
            count += 1

    # 왼쪽 => 오른쪽 대각선이 전체 0인지를 확인
    if bingopan[0][0] + bingopan[1][1] + bingopan[2][2] + bingopan[3][3] + bingopan[4][4] == 0:
        count += 1
    # 오른쪽 => 왼쪽 대각선이 전체 0인지를 확인
    if bingopan[4][0] + bingopan[3][1] + bingopan[2][2] + bingopan[1][3] + bingopan[0][4] == 0:
        count += 1
    # 만약 count가 3이 넘거나 같으면 해당 number가 정답임
    if count >= 3:
        print(number)
        break