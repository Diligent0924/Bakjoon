L, R = input().split()
count = 0
if len(L) != len(R):
    print(0)
else:
    for i in range(len(R)):
        if L[i] == R[i]: # 여기서 L[i] == "8" and R[i] == "8"이 안되는 이유는 8808과 같은 경우에는 끝까지 봐야하므로..
            if L[i] == "8":
                count += 1
        else:
            break
            
    print(count)