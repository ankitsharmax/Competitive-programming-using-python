## Day 3 of competitive programming

- Learnt about space and time complexity
	- Big Oh notation
	- Big Omega notation
	- Theta notation
	
### Q. What is the time complexity

- O(n^3)
- O(n^2)
- O(n^5) = Correct answer
- O(n(n-1))
	
```python
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
```