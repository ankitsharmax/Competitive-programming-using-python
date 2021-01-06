'''
Example Input
2
2 3
2 2
5 5 5
4 3
1 3 2 4
6 7 8

Example Output
2
1

'''


def cheat_vote(n,m):
	sum_n = sum(n)
	sum_m = sum(m)
	if sum_n > sum_m:
		return 0
	else:
		count = 1
		for i in range(min(len(n),len(m))):
			n[i],m[i] = m[i],n[i]
			sum_n_new = sum(n)
			sum_m_new = sum(m)
			if sum_n_new > sum_m_new:
				return count
			else:
				count += 1
		return -1
		
		
T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    N_votes = sorted(list(map(int,input().split())))
    M_votes = sorted(list(map(int,input().split())),reverse=True)
    print(cheat_vote(N_votes,M_votes))
