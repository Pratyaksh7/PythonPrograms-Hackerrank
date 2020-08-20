import numpy as np

n,m,p = list(map(int,input().split()))

array_1 = np.array([list(map(int,input().split())) for _ in range(n)])
array_2 = np.array([list(map(int,input().split())) for _ in range(m)])

print(np.concatenate((array_1,array_2), axis=0))