from collections import Counter
n = int(input())
arr = list(map(int, input().split()))
arr = Counter(arr)
for i in arr:
    print(i, ":", arr[i])
