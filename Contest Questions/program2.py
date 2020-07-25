num, rotation = map(int, input().split())
arr = list(map(str, input().split()))

if rotation < 0:
    value = abs(rotation)
    arr = arr[value:] + arr[:value]

if rotation > 0:
    value = abs(rotation)
    arr = [arr[(i - value) % len(arr)] for i, x in enumerate(arr)]

arr2 = [int(i) for i in arr]
for i in arr2:
    print(i, end=" ")
