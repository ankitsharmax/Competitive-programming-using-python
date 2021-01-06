### Encode String

#### Task: Decode the encoded string

<b>Explanation: </b>How the word is encoded,

For example, the letter ```j``` would be encoded as :

- Among ```(a,b,c,d,e,f,g,h | i,j,k,l,m,n,o,p)```, ```j``` appears in the second half. So the first bit of its encoding is ```1```.
- Now, among ```(i,j,k,l | m,n,o,p)```, ```j``` appears in the first half. So the second bit of its encoding is ```0```.
- Now, among ```(i,j | k,l)```, ```j``` appears in the first half. So the third bit of its encoding is ```0```.
- Now, among ```(i | j)```, ```j``` appears in the second half. So the fourth and last bit of its encoding is ```1```.

So ```j's``` encoding is ```1001```,

![alt text](Explanation.JPG)