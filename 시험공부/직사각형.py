def solution():
    # 점일 때 확인
    for i in rec2:
        if i in rec1:
            return "c"
    # 선일 때
    if c2 == b2 or c1 > a1:
        return 'b'
for test_case in range(4):
    a1, a2, b1, b2, c1, c2, d1, d2 = map(int, input().split())

    rec1 = [(a1, a2), (a1, b2), (b1, a2), (b1, b2)] # 왼쪽 위 / 오른쪽 위 / 왼쪽 아래 / 오른쪽 아래
    rec2 = [(c1, c2), (c1, d2), (d1, c2), (d1, d2)] # 왼쪽 위 / 오른쪽 위 / 왼쪽 아래 / 오른쪽 아래