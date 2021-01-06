'''
Sample Input:
3 -> T
4 -> N
0000 -> S
8 -> N
00001111 -> S
4 -> N
1001 -> S

Sample Output:
a
ap
j

'''



alphs = 'abcdefghijklmnop'

op = len
out = print

def decode(alphs,word):
    a = alphs
    if op(word)>0:
        if word[0] == '0':
            return decode(alphs[:op(alphs)//2],word[1:])
        else:
            return decode(alphs[op(alphs)//2:],word[1:])
    else:
        if word == '1':
            out(alphs[alphs.index(a)+1],end='')
        else:
            out(alphs[alphs.index(a)-1],end='')


T = int(input("Enter test cases: "))
for _ in range(T):
    N = int(input("Enter length of word: "))
    S = input("Enter the encoded string: ")[:N]
    for i in range(0,len(S),4):
        decode(alphs,S[i:i+4])
    print("")
