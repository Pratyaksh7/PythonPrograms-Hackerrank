from itertools import permutations

value = input().split()
S = str.upper(value[0])
k = int(value[1])

print(*[''.join(i) for i in permutations(sorted(S),k)],sep= '\n')
