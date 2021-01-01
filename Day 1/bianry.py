def binary(n):
    till = 2**n
    res = []
    for i in range(till):
        b = bin(i).replace('0b','')
        data = '0'*(n-len(b))
        data += b
        res.append(data)
    print(res)

binary(int(input("Enter lenght of binary value: ")))
