n = int(input())
A=[]
k= input()
list = k.split()

for i in list:
    i= int(i)
    A.append(i)
A=set(A)    
max1 = max(A)

A.remove(max1)

max2=max(A)
print(max2)
        