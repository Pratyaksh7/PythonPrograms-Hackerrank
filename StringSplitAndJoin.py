def split_and_join(line):
    list1= line.split()  # sentence get split in the form of a list
    list1 = "-".join(list1)
    return list1
    
    
line = input()
print(split_and_join(line))