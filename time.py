import datetime, timeit, random
from random import randint

def insertion(A):
    for j in range (1,len(A)):
        key = A[j]
        i = j
        while i>0 and A[i-1] > key:
            A[i] = A[i-1]
            i=i-1
        A[i] = key
    return A

A=random.sample(range(1,1000),500)  #without repetitions

B=[]
for i in range(50):                 #with repetition
    B.append(random.randint(1,10))

C=[]
for i in range(50):                 #increasing
    C.append(random.randint(1,10))
C.sort()

D=[]
for i in range(50):                 #decreasing
    D.append(random.randint(1,10))
D.sort()
D=D[::-1]
    
E=[]
"""for i in range(9):               #"v" shaped
    E.append(0)

index1=0
index2=0
for i in range(10,0,-1):
    if i%2==1:
        E[index1]=i
        index1=index1+1
    else:
        E[index2*(-1)]=i
        index2=index2+1
print (E)"""
E1=[]
E2=[]
for i in range(10):
    E.append(random.randint(1,20))
E.sort()

for i in range(10):
    if i%2==0:
        E1.append(E[i])
    else:
        E2.append(E[i])
E1=E1[::-1]
E=E1+E2
print (E)

start = datetime.datetime.now()
insertion(A)
duration = datetime.datetime.now() - start
DURATION=duration.microseconds

t1 = timeit.Timer(lambda: insertion(A))

print (duration, DURATION)

