def number(n,count):
    global count_list
    if n < 1:
        return
    else:
        count += 1
        list_a = [n-1, n//2, n//3]
        print(count)
        print(list_a)
        if 1 in list_a:
            count_list.append(count)
            return
        else:
            number(n-1,count) # 이게 항상 먼저 들어간다.
            
            if n % 2 == 0:
                number(n//2,count)

            if n % 3 == 0:
                number(n//3,count)
        
count_list = []
N = int(input())
number(N,-1)
print(count_list)