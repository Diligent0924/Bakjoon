N = int(input())
K = int(input())
sensors = sorted(list(map(int, input().split())))
greedy = []
for i in range(1, N):
    greedy.append(sensors[i] - sensors[i-1])
greedy.sort(reverse=True)
print(sum(greedy[K-1:]))