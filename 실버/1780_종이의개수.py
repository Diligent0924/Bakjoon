'''
어떤 재귀 문제가 있을 때 명확하게 몇등분으로 나누게끔 되어있다면 해당 등분만큼 재귀함수를 쓰는 것이 바람직하다.
'''
def solution(start_i, start_j, box_size):
    global result
    number = arr[start_i][start_j]
    if box_size == 1: # 만약 박스사이즈가 1개라면 개수를 한개 추가해주고 끝낸다.
        if number == -1:
            result[0] += 1
        elif number == 0:
            result[1] += 1
        elif number == 1:
            result[2] += 1
        return
    else:
        for i in range(start_i, start_i+box_size):
            for j in range(start_j, start_j+box_size):
                if arr[i][j] != number: # 만약 한개라도 안맞으면 3으로 나눠서 9개로 분할한다.
                    solution(start_i, start_j, box_size//3)
                    solution(start_i, start_j+box_size//3, box_size//3)
                    solution(start_i, start_j+(box_size//3*2), box_size//3)
                    solution(start_i+box_size//3, start_j, box_size//3)
                    solution(start_i+box_size//3, start_j+box_size//3, box_size//3)
                    solution(start_i+box_size//3, start_j+(box_size//3*2), box_size//3)
                    solution(start_i+(box_size//3*2), start_j, box_size//3)
                    solution(start_i+(box_size//3*2), start_j+box_size//3, box_size//3)
                    solution(start_i+(box_size//3*2), start_j+(box_size//3*2), box_size//3)
                    return
        # 만약 중간에 다 맞는 경우가 생긴다면 끝낸다.
        else:
            if number == -1:
                result[0] += 1
            elif number == 0:
                result[1] += 1
            elif number == 1:
                result[2] += 1
            return

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
result = [0,0,0]
solution(0, 0, N)
print(*result)
