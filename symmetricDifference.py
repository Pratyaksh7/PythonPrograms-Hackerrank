M = int(input())
m1 = set(map(int, input().split()))

N = int(input())
n1 = set(map(int, input().split()))

output = list(m1.union(n1).difference(m1.intersection(n1))) 

output.sort()
for i in output:
    print(i)   
