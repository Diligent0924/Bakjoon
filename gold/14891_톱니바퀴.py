tracks = [0]

for i in range(1,5):
    tracks.append([int(i) for i in input()])
# print(tracks)
for _ in range(int(input())):
    number, direction = map(int, input().split()) # direction : 1(시계), -1(반시계)
    # 왼쪽
    left_num,left_direction, left_list = number, direction, [0] * 5
    while left_num >= 2:
        if tracks[left_num - 1][2] != tracks[left_num][6]:
            if left_direction == 1:
                # print(left_num)
                left_list[left_num-1] = -1
                left_direction = -1 # 역방향으로 바꾼다.
            else:
                left_list[left_num-1] = 1
                left_direction = 1 # 정방향으로 바꾼다.
        else: # 만약 안돌았으면 그냥 끝낸다.
            break
        left_num -= 1
    for i in range(1,5):
        if left_list[i] == 1:
            tracks[i].insert(0, tracks[i].pop()) # 시계 방향
        elif left_list[i] == -1:
            tracks[i].append(tracks[i].pop(0)) # 반시계 방향
    # 오른쪽
    right_num, right_direction, right_list = number, direction, [0] * 5
    while right_num <= 3:
        if tracks[right_num+1][6] != tracks[right_num][2]:
            # print(1111111111)
            if right_direction == 1:
                right_list[right_num+1] = -1
                right_direction = -1
            else:
                right_list[right_num+1] = 1
                right_direction = 1
        else:
            break
        right_num += 1
    # print(right_list)
    for i in range(1,5):
        if right_list[i] == 1:
            tracks[i].insert(0, tracks[i].pop()) # 시계 방향
        elif right_list[i] == -1:
            tracks[i].append(tracks[i].pop(0)) # 반시계 방향

    # 해당 톱니바퀴가 돈다. 
    if direction == 1:
        tracks[number].insert(0, tracks[number].pop()) # 시계 방향
    else:
        tracks[number].append(tracks[number].pop(0)) # 반시계 방향
    # print(tracks)   
        
result = 0
w = [0,1,2,4,8]
for i in range(1,5):
    result += tracks[i][0] * w[i]
print(result)