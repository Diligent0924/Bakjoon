import sys
N = int(sys.stdin.readline())
S = int(sys.stdin.readline())
arr = sys.stdin.readline()

count = 0
answer = 'IO' * N + 'I'
a = len(answer)
i = -1
while i < S-a:
    i += 1
    if arr[i] == "I":
        for j in range(i+1,i+a-1,2):
            if arr[j:j+2] != "OI":
                break
        else:
              count += 1
              i += 1
print(count)