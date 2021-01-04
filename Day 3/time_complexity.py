'''
What is the time complexity
1. O(n^3)
2. O(n^2)
3. O(n^5) = correct answer
4. O(n(n-1))
'''
def Func(n):
    for i in range(1,n):
        j = 1
        while j<i*i:
            j+=1
            if j%i==0:
                for k in range(0,j):
                    print("Ankit")

n = int(input())
Func(n)
