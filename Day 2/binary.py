rem = ''

def generate(num):
    global rem
    digits = 3
    if num > 1:
        generate(num//2)
    rem += str(num%2)
    return rem

def test(num,digits):
    out = generate(num)
    if len(out) <= digits:
        return out
    else:
        return "error"

num, digits = map(int,input("Enter space separated num and length of digit: ").split())
print(test(num,digits))
