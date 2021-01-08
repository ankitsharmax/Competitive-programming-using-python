def func(n):
    count = 0
    for j in range(n//2,n): # log(n)
        while j*n//2 <= 2: # log(n)
            k = 1 # 1
            while k<= n: # n/2
                count += 1 # 1
                k = k*2 # 1
            j += 1 # 1
        print(count)

n = int(input())
func(n)
