# 일단 직사각형 껍데기를 만든다. 인덱스는 0 ~ N까지이다.
# 껍데기에서 상점의 위치를 놓는다.
# 반대편으로 갈 경우를 제외하면 나머지는 가까운 순서가 있다.

rec_index, rec_cloumn = map(int, input().split())
N = int(input())
stores = [list(map(int, input().split())) for _ in range(N)]
donggun = list(map(int, input().split()))
result = 0
# 4 3 2 1 => 동 서 남 북
for store in stores:
    if donggun[0] == 4:
        if store[0] == 3:
            result += min(donggun[1] + rec_index + store[1], rec_cloumn - donggun[1] + rec_index + rec_cloumn - store[1])
        elif store[0] == 2:
            result += rec_cloumn - donggun[1] + rec_index - store[1]
        elif store[0] == 1:
            result += donggun[1] + rec_index - store[1]
        else:
            result += abs(store[1] - donggun[1])
    elif donggun[0] == 3:
        if store[0] == 4:
            result += min(donggun[1]+rec_index+store[1], rec_cloumn-donggun[1] + rec_index+ rec_cloumn-store[1])
        elif store[0] == 2:
            result += rec_cloumn - donggun[1] + store[1]
        elif store[0] == 1:
            result += donggun[1] + store[1]
        else:
            result += abs(store[1] - donggun[1])
    elif donggun[0] == 2:
        if store[0] == 4:
            result += rec_index - donggun[1] + rec_cloumn - store[1]
        elif store[0] == 3:
            result += donggun[1] + rec_cloumn - store[1]
        elif store[0] == 1:
            result += min(donggun[1] + rec_cloumn + store[1], rec_index - donggun[1] + rec_cloumn + rec_index - store[1])
        else:
            result += abs(store[1] - donggun[1])
    elif donggun[0] == 1:
        if store[0] == 4:
            result += rec_index - donggun[1] + store[1]
        elif store[0] == 3:
            result += donggun[1] + store[1]
        elif store[0] == 2:
            result += min(rec_index - donggun[1] + rec_cloumn + rec_index - store[1], donggun[1] + rec_cloumn + store[1])
        else:
            result += abs(store[1] - donggun[1])
print(result) 