### Generate binary number based on some conditions

#### Input:
- You're given two inputs N(decimal number) and D(any digit)

- if lenght of binary number <= digits lenght print the binary number
- if lenght of binary number > digits lenght print error

#### Test Case 1:
- Input
```		N, D = 8 4```
- Output
```		1000	  ```

#### Test Case 2:
- Input
```		N, D = 7 2```
- Output
```		error	  ```

#### Explanation
- Test Case 1:
N, D = 8 4
Binary value of 8 is '1000'. Length of binary value of 8 i.e., '1000' is 4 which is <= D

- Test Case 2:
N, D = 7 2
Binary value of 7 is '111'. Length of binary value of 7 i.e., '111' is 3 which is >= D. Therefore it fails to satisfy the condition and prints error