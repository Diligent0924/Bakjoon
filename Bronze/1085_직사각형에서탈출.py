# 직사각형 중 어디가 더 빨리가는지 하는 문제
x,y,w,h = map(int, input().split())

print(min(x,y,w-x,h-y))
