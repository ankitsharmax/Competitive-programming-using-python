## Day 3 of competitive programming

- Learnt about space and time complexity
	- Big Oh notation
	- Big Omega notation
	- Theta notation
	
### Q. What is the time complexity

```python
def func(n):
    count = 0
    for j in range(n//2,n):
        while j*n//2 <= 2:
            k = 1
            while k<= n:
                count += 1
                k = k*2
            j += 1
        print(count)
```