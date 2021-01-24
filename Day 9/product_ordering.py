def test(arr):
    neg = []
    pos = []
    for e in arr:
        if e < 0:
            neg.append(e)
        if e > 0:
            pos.append(e)
        
    neg.sort()
    if len(neg)>2:
        if len(neg)%2 != 0:
            neg.pop()
    res = 1
    for e in neg:
        res *= e
    for e in pos:
        res *= e

    if len(neg)==0 and len(pos)==0:
        print(0)
    else:
        print(res)

test([0,0,0,0,0,0])
test([2,0,2,2,0])
test([-2,-3,4,-5])
test([-6])
test([2,6,0,-1,-34,-1,5])
test([1,3,0])
