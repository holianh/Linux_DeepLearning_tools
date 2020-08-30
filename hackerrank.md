# giải bài tập trong Hackerrank.com phần Python

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

## Nested Lists

```python

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




