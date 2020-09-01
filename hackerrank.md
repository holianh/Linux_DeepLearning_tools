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
<span class="MathJax_SVG" id="MathJax-Element-6-Frame" style="border: 0px; direction: ltr; display: inline-block; float: none; font-family: inherit; font-stretch: inherit; font-variant: inherit; line-height: normal; margin: 0px; max-height: none; max-width: none; min-height: 0px; min-width: 0px; outline: 0px; overflow-wrap: normal; padding: 0px; vertical-align: baseline; white-space: nowrap; word-spacing: normal;"><svg focusable="false" height="3.176ex" role="img" style="vertical-align: -0.838ex;" viewBox="0 -1006.6 7822 1367.4" width="18.167ex" xmlns:xlink="http://www.w3.org/1999/xlink"><g fill="currentColor" stroke-width="0" stroke="currentColor" transform="matrix(1 0 0 -1 0 0)"><path d="M94 250Q94 319 104 381T127 488T164 576T202 643T244 695T277 729T302 750H315H319Q333 750 333 741Q333 738 316 720T275 667T226 581T184 443T167 250T184 58T225 -81T274 -167T316 -220T333 -241Q333 -250 318 -250H315H302L274 -226Q180 -141 137 -14T94 250Z" stroke-width="1"></path><g transform="translate(389,0)"><path d="M213 578L200 573Q186 568 160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285 666Q294 666 302 660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100 0H88V46H114Q136 46 152 46T177 47T193 50T201 52T207 57T213 61V578Z" stroke-width="1"></path><path d="M96 585Q152 666 249 666Q297 666 345 640T423 548Q460 465 460 320Q460 165 417 83Q397 41 362 16T301 -15T250 -22Q224 -22 198 -16T137 16T82 83Q39 165 39 320Q39 494 96 585ZM321 597Q291 629 250 629Q208 629 178 597Q153 571 145 525T137 333Q137 175 145 125T181 46Q209 16 250 16Q290 16 318 46Q347 76 354 130T362 333Q362 478 354 524T321 597Z" stroke-width="1" transform="translate(500,0)"></path><g transform="translate(1001,393)"><path d="M42 313Q42 476 123 571T303 666Q372 666 402 630T432 550Q432 525 418 510T379 495Q356 495 341 509T326 548Q326 592 373 601Q351 623 311 626Q240 626 194 566Q147 500 147 364L148 360Q153 366 156 373Q197 433 263 433H267Q313 433 348 414Q372 400 396 374T435 317Q456 268 456 210V192Q456 169 451 149Q440 90 387 34T253 -22Q225 -22 199 -14T143 16T92 75T56 172T42 313ZM257 397Q227 397 205 380T171 335T154 278T148 216Q148 133 160 97T198 39Q222 21 251 21Q302 21 329 59Q342 77 347 104T352 209Q352 289 347 316T329 361Q302 397 257 397Z" stroke-width="1" transform="scale(0.707)"></path></g></g><g transform="translate(1844,0)"><path d="M423 750Q432 750 438 744T444 730Q444 725 271 248T92 -240Q85 -250 75 -250Q68 -250 62 -245T56 -231Q56 -221 230 257T407 740Q411 750 423 750Z" stroke-width="1"></path></g><g transform="translate(2594,0)"><path d="M352 287Q304 211 232 211Q154 211 104 270T44 396Q42 412 42 436V444Q42 537 111 606Q171 666 243 666Q245 666 249 666T257 665H261Q273 665 286 663T323 651T370 619T413 560Q456 472 456 334Q456 194 396 97Q361 41 312 10T208 -22Q147 -22 108 7T68 93T121 149Q143 149 158 135T173 96Q173 78 164 65T148 49T135 44L131 43Q131 41 138 37T164 27T206 22H212Q272 22 313 86Q352 142 352 280V287ZM244 248Q292 248 321 297T351 430Q351 508 343 542Q341 552 337 562T323 588T293 615T246 625Q208 625 181 598Q160 576 154 546T147 441Q147 358 152 329T172 282Q197 248 244 248Z" stroke-width="1"></path></g><g transform="translate(3095,0)"><path d="M60 749L64 750Q69 750 74 750H86L114 726Q208 641 251 514T294 250Q294 182 284 119T261 12T224 -76T186 -143T145 -194T113 -227T90 -246Q87 -249 86 -250H74Q66 -250 63 -250T58 -247T55 -238Q56 -237 66 -225Q221 -64 221 250T66 725Q56 737 55 738Q55 746 60 749Z" stroke-width="1"></path></g><g transform="translate(3762,0)"><path d="M56 347Q56 360 70 367H707Q722 359 722 347Q722 336 708 328L390 327H72Q56 332 56 347ZM56 153Q56 168 72 173H708Q722 163 722 153Q722 140 707 133H70Q56 140 56 153Z" stroke-width="1"></path></g><g transform="translate(4818,0)"><path d="M213 578L200 573Q186 568 160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285 666Q294 666 302 660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100 0H88V46H114Q136 46 152 46T177 47T193 50T201 52T207 57T213 61V578Z" stroke-width="1"></path><path d="M213 578L200 573Q186 568 160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285 666Q294 666 302 660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100 0H88V46H114Q136 46 152 46T177 47T193 50T201 52T207 57T213 61V578Z" stroke-width="1" transform="translate(500,0)"></path><path d="M213 578L200 573Q186 568 160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285 666Q294 666 302 660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100 0H88V46H114Q136 46 152 46T177 47T193 50T201 52T207 57T213 61V578Z" stroke-width="1" transform="translate(1001,0)"></path><path d="M213 578L200 573Q186 568 160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285 666Q294 666 302 660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100 0H88V46H114Q136 46 152 46T177 47T193 50T201 52T207 57T213 61V578Z" stroke-width="1" transform="translate(1501,0)"></path><path d="M213 578L200 573Q186 568 160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285 666Q294 666 302 660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100 0H88V46H114Q136 46 152 46T177 47T193 50T201 52T207 57T213 61V578Z" stroke-width="1" transform="translate(2002,0)"></path><path d="M213 578L200 573Q186 568 160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285 666Q294 666 302 660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100 0H88V46H114Q136 46 152 46T177 47T193 50T201 52T207 57T213 61V578Z" stroke-width="1" transform="translate(2502,0)"></path></g></g></svg></span>

```python
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print ((10**i//9)**2)
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




