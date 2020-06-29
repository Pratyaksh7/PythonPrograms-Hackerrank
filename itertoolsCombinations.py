from itertools import combinations
n = input().split()
string = n[0].upper()
k = int(n[1])

for i in range(1,k+1):
    for c in combinations(sorted(string), i):
        print(''.join(c))