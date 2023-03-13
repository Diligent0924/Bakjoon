'''
1. 선을 미리 저장한다. (선의 개수, 선의 방향)
2. 전체를 90도로 꺾을 때를 확인하여 반복한다.
3. 전체 point를 만든 후에 전체를 탐색하며 확인한다. (자기 기준으로 4방향을 확인)
'''
N = int(input())
arr = [[0] * 100 for _ in range(100)] # x,y 좌표를 100 X 100 형태로 나타낸다.
delta = (0,1),(-1,0),(0,-1),(1,0) # 순서대로 넣는다.

for _ in range(N):
    y,x,d,g = map(int, input().split())
    # 처음인 점을 넣는다.
    
    # 제일 처음일 때는 넣는다.
    a, b = 
    count = 0
    stack = []
    while True:
        count += 1
        
        
        if count == d:
            break