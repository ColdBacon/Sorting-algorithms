class Stack:
    def __init__(self):
        self.stack = []

    def push(self, a, b):
        self.stack.append((a, b))

    def pop(self):
        a = self.stack.pop(- 1)
        return a

    def top(self):
        return self.stack[len(self.stack)-1]

    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

def QS(A):
    stos = Stack()
    stos.push(0, len(A)-1)
    while not stos.empty():
        p, r = stos.pop()
        while p < r:
            x=A[(p+r)//2]
            i=p
            j=r
            while i<j:
                while A[i]<x:
                    i=i+1
                while A[j]>x:
                    j=j-1
                if i<=j:
                    A[i], A[j]=A[j], A[i]
                    i=i+1
                    j=j-1
            if i<r:
                stos.push(i, r)
            r = j
    return A

A=[3, 5, 2, 9, 7, 10, 1]
print(QS(A))
