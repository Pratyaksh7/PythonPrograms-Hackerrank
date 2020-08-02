from collections import Counter
x = int(input())

shoe_sizes = map(int, input().split())
shoes = Counter(shoe_sizes)
n = int(input())
money = 0
for i in range(n):
    size, price = map(int, input().split())
    if shoes[size]:
        money += price
        shoes[size] -= 1

print(money)
