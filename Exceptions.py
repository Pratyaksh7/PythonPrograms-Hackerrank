T = int(input())
for i in range(T):
    try:
        a, b = map(str, input().split())
        print(int(int(a)//int(b)))
    except Exception as e:
        print("Error Code:", e)
