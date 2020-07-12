n , m = map(int, input().split())

array = list(map(int, input().split()))

A = list(set(map(int, input().split())))
B = list(set(map(int, input().split())))

happiness = 0

for i in range(n):
    for j in range(m):
        if array[i] == A[j]:
            happiness += 1
            
        elif array[i] == B[j]:
            happiness -= 1  
        
print(happiness)        
