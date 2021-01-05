'''
Sample Input:
5
1 5 31
4
1 10 3
23
2 5 7
20 36
2 5 10
19 2
3 3 300
1 1 1

Sample Output:
0
2
7
4
1
'''



T = int(input())
s = sum
for _ in range(T):
    N,K,D = map(int,input().split())
    A = list(map(int,input().split()))[:N]
    sum_of_A = s(A)
    if sum_of_A < K :
        print(0)
    else:
        possible = sum_of_A//K
        if possible > D:
            print(D)
        else:
            print(possible)
        
    
    
