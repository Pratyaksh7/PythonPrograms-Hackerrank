def mutate_string(string1, i, c):
    string1 = list(string1)
    string1[i] = c
    string1 = "".join(string1)
    print(string1)

string1 = input()
i, c = input().split()

new_string = mutate_string(string1, int(i), c)
