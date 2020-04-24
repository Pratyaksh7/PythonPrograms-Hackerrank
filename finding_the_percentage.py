N = int(input())
A = {}
for i in range(1,N+1):
    line = input().split()
    A[line[0]] = sum(map(float,line[1:]))/3
    
name=input()
print('%.2f' % A[name])