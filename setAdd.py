n = int(input())

countries = []
for i in range(n):
    countries.append(input())
    
print(len(set(countries)))    