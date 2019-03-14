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

start = datetime.datetime.now()
insertion(A)
duration = datetime.datetime.now() - start
DURATION=duration.microseconds

t1 = timeit.Timer(lambda: insertion(A))

print (duration, DURATION)

