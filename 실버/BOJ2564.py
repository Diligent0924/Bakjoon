H, V = map(int, input().split()) # H : 가로 / V : 세로
stores = [tuple(map(int, input().split())) for _ in range(int(input()))]
dong = tuple(map(int, input().split())) # 동근이의 위치

exp = {
    (1, 2): (lambda x: min(x[0] + x[1], 2*H - (x[0] + x[1])) + V), 
    (1, 3): (lambda x: x[0] + x[1]), 
    (1, 4): (lambda x: H - x[0] + x[1]), 
    (2, 3): (lambda x: x[0] + (V - x[1])), 
    (2, 4): (lambda x: (H - x[0]) + (V - x[1])),
    (3, 4): (lambda x: min(x[0] + x[1], 2*V - (x[0] + x[1])) + H), 
}

d = 0
for store in stores:
    if dong[0] == store[0]:
        d += abs(dong[1] - store[1])
    else:
        (p1, d1), (p2, d2) = sorted((store, dong))
        d += exp[(p1, p2)]((d1, d2))
    
print(d)