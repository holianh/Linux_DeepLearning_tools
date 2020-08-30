# giải bài tập trong Hackerrank.com phần Python

## 

```python

```

## 

```python

```

## 

```python

```

## 

```python

```

## Merge the Tools!
https://www.hackerrank.com/challenges/merge-the-tools/problem
```python
def merge_the_tools(string, k):
    print("\n".join( [''.join([si for n, si in enumerate(string[i:i+k]) if si not in string[i:i+k][:n]] ) for i in range(0,len(string),k) ]))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
```

## The Minion Game
https://www.hackerrank.com/challenges/the-minion-game/problem
```python
def minion_game(string): 
    vowel =['A','E','I','O','U']
    S=0
    K=0
    for i in range(len(string)):
        if string[i] in vowel:
            K+= len(string)-i
        else:
            S+=len(string)-i
    if S>K:
        print("Stuart"+" "+ "%d" % S)
    elif K>S:
        print("Kevin"+" "+'%d' % K)
    else:
        print("Draw")
    

if __name__ == '__main__':
    s = input()
    minion_game(s)
```

## Capitalize
https://www.hackerrank.com/challenges/capitalize/problem
```python
import string 
def solve(s):
    s=''.join( (c.upper() if i == 0 or s[i-1] == ' ' else c) for i, c in enumerate(s) )
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

```


## Alphabet Rangoli
https://www.hackerrank.com/challenges/alphabet-rangoli/problem
```python
import string
def print_rangoli(size):
    alpha = string.ascii_lowercase
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))
```


## String Formatting
https://www.hackerrank.com/challenges/python-string-formatting/problem
```python
def print_formatted(n):
    width = len("{0:b}".format(n))
    for i in range(1,n+1):
        print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
```


## Designer Door Mat
https://www.hackerrank.com/challenges/designer-door-mat/problem
```python
N, M = [int(k) for k in input().split()]
for line in range(N//2): print( (".|."*(2*line+1)).center(M,'-'))
print( "WELCOME".center(M,'-'))
for line in range(N//2,0,-1): print( (".|."*(2*line-1)).center(M,'-'))

#-------------------------
n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

```


## Text Wrap
https://www.hackerrank.com/challenges/text-wrap/problem
```python
import textwrap

def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string,max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
```


## String Validators
https://www.hackerrank.com/challenges/string-validators/problem
```python
if __name__ == '__main__':
    st = input()
    kq=[0,0,0,0,0 ]
    for s in st:
        if s.isalnum(): kq[0]=1
        if s.isalpha(): kq[1]=1
        if s.isdigit(): kq[2]=1
        if s.islower(): kq[3]=1
        if s.isupper(): kq[4]=1
    for k in kq:
        print(bool(k))
#---------------
s = input()
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))
```


## Find a string
https://www.hackerrank.com/challenges/find-a-string/problem
```python
line, target = [input() for _ in range(2)]
score = 0
for i in range(len(line)):
   if line[i:i+len(target)] == target:
        score += 1
print (score)
```


## sWAP cASE
https://www.hackerrank.com/challenges/swap-case/problem
```python
# print ''.join([i.lower() if i.isupper() else i.upper() for i in raw_input()])

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
```



## What's Your Name?
https://www.hackerrank.com/challenges/whats-your-name/problem
```python
def print_full_name(a, b):
    print(f"Hello {a} {b}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
```


## Python If-Else
https://www.hackerrank.com/challenges/py-if-else/problem
```python
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n%2==1: 
        print('Weird');
    else:
        if 2<=n<=5:
            print('Not Weird')
        if 6<=n<=20:
            print('Weird')
        if 20<n:
            print('Not Weird')
```

## Tuples
https://www.hackerrank.com/challenges/python-tuples/problem
```python
if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))
```    

## Find the Runner-Up Score!
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
```python
if __name__ == '__main__':
    n = int(input())
    arr =list( map(int, input().split()))
   
    nmax,nsec = max(arr),-1000
    for k in arr:
        if (nsec<k)and k<nmax:
            nsec=k
    print(nsec) 
```

## Nested Lists
https://www.hackerrank.com/challenges/nested-list/problem
```python
if __name__ == '__main__':
    AllStudents=[]
    minGrade=None
    for _ in range(int(input())):
        name = input()
        score = float(input())
        oneStudent=[name,score]
        AllStudents.append(oneStudent)
        minGrade=score if minGrade==None else min(minGrade,score)

    AllStudents=sorted(AllStudents, key=lambda x: x[0])

    value=min([score for name, score in AllStudents if score>minGrade])
    
    for name,score in AllStudents:
        if score==value:
            print(name)
```

## List Comprehensions
https://www.hackerrank.com/challenges/list-comprehensions/problem
```python
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    s=[[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if (a+b+c)!=n]
    print(s)
```

## Finding the percentage
https://www.hackerrank.com/challenges/finding-the-percentage/problem
```python
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("{:.2f}".format(sum(student_marks[query_name])/len(student_marks[query_name])))
```
## Validating phone numbers
https://www.hackerrank.com/challenges/validating-the-phone-number/problem

```python
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        mystr = input()
        match = re.search(r'^[789]\d\d\d\d\d\d\d\d', mystr)
        if match and len(mystr)==10:
            print ("YES")
        else:
            print("NO")
```
## Validating and Parsing Email Addresses
https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

```python
import re
n = int(input())
for _ in range(n):
    x, y = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if m:
        print(x,y)
```            


## Word Order
đề:
https://www.hackerrank.com/challenges/word-order/problem


```python
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
d={}
q=[]
for k in range(n):
    key=input()
    d[key]=d.get(key,0)+1
    q.append(key)    

print(len(d))
inroi=[]
for key in q:
    if not key in inroi:
        print(d[key], end=' ')
        inroi+=[key]
```




