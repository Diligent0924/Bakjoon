import sys
bingopan = [list(map(int, input().split())) for _ in range(5)]
sahepan = []
for i in range(5):
    sahepan.extend(list(map(int, input().split())))
result, count,True_list = 0, 0, [0,0,0,0,0]
bingopan_1,bingopan_2,bingopan_dajat,bingopan_dajat_T = [], [], False,False
count_list = []
for i in sahepan:
    result += 1
    for j in range(len(bingopan)):
        for h in range(len(bingopan)): 
            if i == bingopan[j][h]:
                bingopan[j][h] = 0
                bingopan_T = list(map(list, zip(*bingopan)))
                for n in range(len(bingopan)):
                    if bingopan[n] == True_list and n not in bingopan_1:
                        bingopan_1.append(n)
                        count += 1
                    if bingopan_T[n] == True_list and n not in bingopan_2:
                        bingopan_2.append(n)
                        count += 1
                if [bingopan[0][0], bingopan[1][1], bingopan[2][2], bingopan[3][3], bingopan[4][4]] == True_list and bingopan_dajat == False:
                    bingopan_dajat = True
                    count += 1
                if [bingopan[0][4], bingopan[1][3], bingopan[2][2], bingopan[3][1], bingopan[0][4]] == True_list and bingopan_dajat_T == False:
                    bingopan_dajat_T = True
                    count += 1
                if count >= 3:
                    print(result)
                    sys.exit()