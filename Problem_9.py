import numpy as np
n=int(input("No.of Rows:"))
m=int(input("No.of Coloums:"))
A=np.random.randint(0,10,size=(n,m))
B=np.random.randint(0,10,size=(n,m))
print(A)
print(B)
print(np.mean(A))
normilzed_A=9*(A-np.min(A))/(np.max(A)-np.min(A))
print(normilzed_A)
a,b,x,y=1,1,1,1
print(A[a:b+1,x:y+1])
print(A[a:b+1,:])