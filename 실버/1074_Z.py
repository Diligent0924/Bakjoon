import sys

def partition_2(start_i, start_j, box_size):
    global count
    if r < start_i or r >= start_i + box_size or c < start_j or c >= start_j + box_size:
        count += box_size * box_size
        return
    if box_size == 2:
        if (r, c) in ((start_i,start_j), (start_i,start_j+1), (start_i+1,start_j), (start_i+1, start_j+1)):
            for dr, dc in ((start_i,start_j), (start_i,start_j+1), (start_i+1,start_j), (start_i+1, start_j+1)):
                count += 1
                if r == dr and c == dc:
                    print(count)
                    sys.exit()
                    return
        else:
            count += 4
            return
    else:
        partition_2(start_i, start_j, box_size//2)
        partition_2(start_i, start_j+box_size//2, box_size//2)
        partition_2(start_i+box_size//2, start_j, box_size//2)
        partition_2(start_i+box_size//2, start_j+box_size//2, box_size//2)
        return



N, r, c = map(int, input().split())
count = -1
partition_2(0, 0, 2**N)