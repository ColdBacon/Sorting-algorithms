#INSERTION SORT
def insertion(A):
    for j in range (1,len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i] > key:
            A[i+1] = A[i]
            i=i-1
        A[i+1] = key
    return A

#SELECTION SORT
def selection (A):
    for j in range (len(A)-1,0,-1):
        maxi=j
        for i in range (j-1,-1,-1):
            if A[i] > A[maxi]:
                maxi=i
        A[j],A[maxi]= A[maxi],A[j]
    return A

#HEAP SORT
def heapfy(A,i,heapsize):
    largest = i
    l=2*i+1
    r=2*i+2
    if l < heapsize and A[l] > A[i]:
        largest = l
        
    if r < heapsize and A[r] > A[largest]:
        largest = r
        
    if largest != i:
        A[i],A[largest]=A[largest],A[i]
        heapfy(A,largest,heapsize)

#The main function to sort an array of given size

def buildheap_main (A):
    heapsize = len(A)
    
    #Build max heap
    for i in range (len(A),-1,-1):
        heapfy(A,i,heapsize)

    # One by one extract elements
    for i in range (len(A)-1,0,-1):
        A[0],A[i]=A[i],A[0]
        heapsize = heapsize - 1
        heapfy(A,0,heapsize)
    return A

#QUICK SORT
from random import randint
def quicksort_main(A):
   quicksort(A,0,len(A)-1)
   return A

def quicksort(A,p,r):
   if p < r:
      q=partition(A,p,r)
      quicksort(A,p,q)
      quicksort(A,q+1,r)

def partition(A,p,r):
   piv = randint(p,r)
   x=A[piv]

   i=p-1
   j=r+1

   while True:
      i=i+1
      j=j-1

      while A[i]<x:
         i=i+1

      while A[j]>x:
         j=j-1

      if i<j:
         A[i],A[j]=A[j],A[i]
      else:
         return j

#MERGE SORT
def ms_main(l, r, A):
    B=[]
    for i in range(len(A)):
        B.append(0)
    mergesort(A, 0, len(A)-1, B)
    m=(l+r)//2
    if l<r:
        ms_main(l, m, A)
        ms_main(m+1, r, A)
        mergesort(A, l, r, B)
    return A

def mergesort(A, l, r, B):
    m=(l+r)//2
    if m-1>0:
        mergesort(A, 1, m, B)
    if r-m>1:
        mergesort(A, m+1, r, B)

    i=l
    j=m+1
    for k in range(l, r+1):
        if (i<=m and j>r) or (i <=m and j<=r and A[i] <= A[j]):
            B[k] = A[i]
            i+=1
        else:
            B[k] = A[j]
            j+=1

    for k in range(l, r+1):
        A[k]=B[k]
