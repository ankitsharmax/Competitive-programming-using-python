def append(s,arr):
    return [s+x for x in arr]

def generate(n):
    if n == 0: return []
    if n == 1: return ['0','1']
    else:
        return (append('0',generate(n-1))+
                append('1',generate(n-1)))

for i in range(1,4):
    print(f'{i} :',generate(i))
