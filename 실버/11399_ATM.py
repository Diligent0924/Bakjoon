N = int(input())
arr = list(map(int, input().split()))
# new_arr = []
# for i in range(N):
#     new_arr.append((i+1, arr[i]))
#
# new_arr = sorted(new_arr, key=lambda x: x[1])
arr.sort()
stack = []
for i in arr:
    if not stack:
        stack.append(i)
    else:
        stack.append(stack[-1] + i)
print(sum(stack))