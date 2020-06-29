from itertools import combinations_with_replacement

n = input().split()
string = n[0].upper()
k = int(n[1])

for i in combinations_with_replacement(sorted(string), k):
    print(''.join(i))