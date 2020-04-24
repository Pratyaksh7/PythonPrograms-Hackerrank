A={}
n=int(input())

for i in range(0,n):
    name=input()
    score = float(input())
    if score in A:
        A[score].append(name)
    else:
        A[score] = [name]
list1 = []
for i in A:
    list1.append([i,A[i]])
list1.sort()

result= list1[1][1]
result.sort()              #if same score then it will sort the name alphabetically
print(result, sep="\n")       
    