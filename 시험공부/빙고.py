bingopan = [list(map(int, input().split())) for _ in range(5)]
answer = []
for _ in range(5):
    answer.extend(list(map(int, input().split())))

answer_sheet = [[0]*5 for _ in range(5)]
answer_count = 0
for i in answer:
    answer_count += 1
    # 빙고판에서 하나씩 찾아보기
    for sero in range(5):
        for garo in range(5):
            if bingopan[sero][garo] == i:
                answer_sheet[sero][garo] = 1
    # 빙고된 수가 몇개인지 확인하기.
    count = 0
    # 가로
    for sero in range(5):
        if sum(answer_sheet[sero]) == 5:
            count += 1
    # 세로
    answer_sheet_T = list(map(list, zip(*answer_sheet)))
    for sero in range(5):
        if sum(answer_sheet_T[sero]) == 5:
            count += 1
    # 대각선
    a = 0
    for i in range(5):
        for j in range(5):
            if i == j and answer_sheet[i][j] == 1:
                a += 1
    if a == 5:
        count += 1

    b= 0
    for i in range(5):
        for j in range(5):
            if i + j == 4 and answer_sheet[i][j] == 1:
                b += 1
    if b == 5:
        count += 1

    # 빙고판 확인하기
    if count >= 3:
        print(answer_count)
        break