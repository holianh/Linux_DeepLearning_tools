# Vài điều cần biết khó tìm
## Ký hiệu một và hai dấu *
An asterisk * denotes iterable unpacking. Its operand must be an iterable. The iterable is expanded into a sequence of items, which are included in the new tuple, list, or set, at the site of the unpacking.

A double asterisk ** denotes dictionary unpacking. Its operand must be a mapping. Each mapping item is added to the new dictionary. Later values replace values already set by earlier key/datum pairs and earlier dictionary unpackings.

Tham khảo: [ở đây](https://docs.python.org/3/reference/expressions.html?highlight=list#expression-lists)

Giải thích thêm:

About the unpack operator * in \*product(a, b), please kindly refer to [Expression lists|Python Documentation](https://docs.python.org/3/reference/expressions.html?highlight=list#expression-lists) and it further refers to [PEP 448](https://www.python.org/dev/peps/pep-0448/) with clear examples. For dictionary, the unpacker operator is ** instead. Thanks for the great Python.

Thử với [Python Online](https://repl.it/languages/python3)
```python
>>> print(*[1], *[2], 3)
1 2 3
>>> arr = [1, 2, 3]
>>> print(*arr) # unpack arr --> print(1, 2, 3)

>>> dict(**{'x': 1}, y=2, **{'z': 3})
{'x': 1, 'y': 2, 'z': 3}
```
Tham khảo: [tại đây](https://www.hackerrank.com/challenges/itertools-product/forum)

# giải bài tập trong Hackerrank.com phần Python

# Math

## Polar Coordinates
https://www.hackerrank.com/challenges/polar-coordinates/problem
```python
from cmath import phase 
z=input() # a | bj | a+bj
z=complex(z)
r   =abs(z)
phi =phase(z)
print(r)
print(phi)
```

## Find Angle MBC
https://www.hackerrank.com/challenges/find-angle/problem
```python
import math
ab=int(input())
bc=int(input())
print(f"{round(180*math.atan(ab/bc)/math.pi)}°")
```

## Triangle Quest 2
https://www.hackerrank.com/challenges/triangle-quest-2/problem
```
10^1/9=1
10^2/9=11
10^3/9=111
10^4/9=1111
...
và
1*1=1
11*11=121
111*111=12321
1111*1111=1234321
...
```
```python
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print ((10**i//9)**2)
```

## Mod Divmod
https://www.hackerrank.com/challenges/python-mod-divmod/problem
```python
a=int(input())
b=int(input())
print(f"{a//b}\n{a%b}\n{divmod(a,b)}")
```

## Power - Mod Power
https://www.hackerrank.com/challenges/python-power-mod-power/problem
```python
a,b,m=[int(input()) for _ in range(3)]
print("{}\n{}".format(pow(a,b),pow(a,b,m)))
```

## Integers Come In All Sizes
https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem
```python
a,b,c,d=[int(input()) for _ in range(4)]
print(a**b+c**d)
```

## Triangle Quest
https://www.hackerrank.com/challenges/python-quest-1/problem
```python
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(round(i*(10**i//9)))
```

# itertools

## itertools.product()
https://www.hackerrank.com/challenges/itertools-product/problem
```python
A=list(map(int,input().split()))
B=list(map(int,input().split()))
from itertools import product
for a in list(product(A,B)): print("{} ".format(a), end='')
#--------------------------------
from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*product(a, b))
```

## permutations
https://www.hackerrank.com/challenges/itertools-permutations/problem
```python
s,t=input().split()
from itertools import permutations
s=sorted([''.join(list(a)) for a in list(permutations(s,int(t)))])
for kq in s:print(kq)
#------------------------------------
from itertools import permutations
s,n = input().split()
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')
```

## itertools.combinations()
https://www.hackerrank.com/challenges/itertools-combinations/problem
```python
s,T=input().split()
from itertools import combinations
 
s=[[''.join(list(a)) for a in list(combinations(sorted(s),int(t)))]
for t in range(1,int(T)+1)]
for kq in s:print(*kq,sep='\n')
#---------------------------------------------
from itertools import combinations
a,b = input().split()
print(*[''.join(j) for i in range(1,int(b)+1) for j in combinations(sorted(a),i)],sep='\n')
#---------------------------------------------
import itertools
s = input().split()
string, number = sorted(s[0]), int(s[1])
for i in range(1, number + 1):
    print(*list(map(''.join, itertools.combinations(string, i))), sep='\n')
#----------------------------------------------------
from itertools import *
s,k = input().split()
for l in range(1,int(k)+1):
    for c in combinations (sorted(s),l):
        print(''.join(c))
```

## itertools.combinations_with_replacement()
https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
```python
s,t=input().split()
from itertools import combinations_with_replacement
s=sorted([''.join(list(a)) for a in list(combinations_with_replacement(sorted(s),int(t)))])
for kq in s:print(kq)
```
##   Compress the String!
https://www.hackerrank.com/challenges/compress-the-string/problem
```python
from itertools import groupby
print(*[(len(list(g)), int(k)) for k, g in groupby(input())]) 
# 'AAAABBBCCD' --> k:'A', g:'AAAA' => AAAA BBB CC D
```

##   Iterables and Iterators
https://www.hackerrank.com/challenges/iterables-and-iterators/problem

```python
from itertools import combinations 

N = int(input())
S = raw_input().split(' ')
K = int(input())

num = 0
All = 0

for c in combinations(S,K):
    All+=1
    num+='a' in c
    
print float(num)/All
#------------------------------------------------------------
from math import factorial as fact

n,aCount,k = int(input()), input().count('a'), int(input())

combs = fact(n) // fact(n-k) if n>=k else 0
without = fact(n-aCount) // fact((n-aCount)-k) if (n-aCount)>=k else 0

print(1-(without / combs) if combs else 0)

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
##   

```python

```
##   

```python

```


## The Captain's Room
https://www.hackerrank.com/challenges/py-the-captains-room/problem
```python
K=int(input())
Rooms=sorted(list(map(int,input().split())))
groups = [Rooms[x:x+K] for x in range(0, len(Rooms), K)]
 
found=False
for family in groups:
    if len(set(family))>1:
        print(family[0])
        found=True
        break
if not found:
    print(Rooms[-1])

```
Chúng tôi chỉ đơn giản tính toán sự khác biệt về tổng sẽ là bao nhiêu nếu có K phần tử của tất cả các nhóm. Chúng tôi sẽ còn lại k-1 * số phòng đội trưởng, chúng tôi chỉ cần chia cho k-1 để có câu trả lời.
```python
k,arr = int(input()),list(map(int, input().split()))
myset = set(arr)
print(((sum(myset)*k)-(sum(arr)))//(k-1))
```


## Set Mutations
https://www.hackerrank.com/challenges/py-set-mutations/problem
```python
n=input()
A=set(map(int,input().split()))

m=int(input())
for k in range(m):
    cmd=input().split()[0]
    B=set(map(int,input().split()))
    eval(f'A.{cmd}(B)')
print(sum(A))


```

## union

```python
n=input()
A=set(map(int,input().split()))
m=input()
B=set(map(int,input().split()))
print(len(B.union(A)))
```

## Set .discard(), .remove() & .pop()
https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
```python
n = int(input())
s = set(map(int, input().split()))
nCmd=int(input())
for k in range(nCmd):
    CMD=input().split()+['']
    cmd, num=CMD[0], CMD[1]
    eval(f's.{cmd}({num})')    
print(sum(s))
#-------------------------------
n = int(input())
s = set(map(int, input().split())) 
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))
```

## Set .add()
https://www.hackerrank.com/challenges/py-set-add/problem
```python
n=int(input())
mySet=set()
for k in range(n):
    mySet.add(input())
print(len(mySet))    
```

## Symmetric Difference
https://www.hackerrank.com/challenges/symmetric-difference/problem

```python
nN = int(input())
arrN = set(map(int, input().split()))

nM = int(input())
arrM = set(map(int, input().split()))

diff = list(arrN.difference(arrM))
diff +=list(arrM.difference(arrN))
for k in sorted(list(diff)):
    print(k)

```

## No Idea!
https://www.hackerrank.com/challenges/no-idea/problem
```python
# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

Happy=0
for arr1 in arr:
    if arr1 in A: Happy+=1
    if arr1 in B: Happy-=1
print(Happy)

```

## Introduction to Sets
https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
```python
def average(array):
    if len(array)==0:return None
    myset=set(array)
    return sum(myset)/len(myset)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
```

## Merge the Tools!
https://www.hackerrank.com/challenges/merge-the-tools/problem
```python
def merge_the_tools(string, k):
    print("\n".join( [''.join([si for n, si in enumerate(string[i:i+k]) if si not in string[i:i+k][:n]] ) for i in range(0,len(string),k) ]))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
#----------------------------------
from collections import OrderedDict

def merge_the_tools(string, k):
    for x in range(0,len(string),k):     
        print(''.join(list(OrderedDict.fromkeys(string[x:x+k]))))
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
marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
#-------------------------------------------------------------------------
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




