n = int(input())
arr=[]
for i in range(n):
    string1= input().split()         # for taking the command and their respective inputs        
    for i in range(1,len(string1)):
        string1[i] = int(string1[i])
        
    if string1[0] == 'insert':
      arr.insert(string1[1], string1[2])
    elif string1[0] == 'print':
        print(arr)
    elif string1[0] == 'remove':
        arr.remove(string1[1])
    elif string1[0] == 'append':
        arr.append(string1[1])
    elif string1[0] == 'sort':
        arr.sort()
    elif string1[0] == 'pop':
        arr.pop()
    elif string1[0] == 'reverse':
        arr.reverse()
            