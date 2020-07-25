A = int(input())
B = int(input())

even = []
odd = []
if A >= 1 and B >= 1:
    for i in range(A, B+1):
        if (i % 10) % 2 == 0 and (i // 10) % 2 == 0:
            even.append(i)
        elif (i % 10) % 2 != 0 and (i // 10) % 2 != 0:
            odd.append(i)
    for i in odd:
        print(i, end=" ")

    print()
    for i in even:
        print(i, end=" ")
