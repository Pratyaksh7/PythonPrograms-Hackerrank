string1 = input().strip()  #strip is used to copy the string but can delete the string/characrter from the parent string given in its args 
substring = input().strip()
count = 0

for i in range(len(string1)-len(substring) +1):
    if string1[i: i+len(substring)] == substring:
        count+=1
        
print(count)        
   
#######################3 In The Form Of A Function#################
 


# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string)-len(sub_string) +1):
#         if string[i: i+len(sub_string)] == sub_string:
#             count+=1
#     return count

# string = input().strip()
# sub_string = input().strip()
    
# count = count_substring(string, sub_string)
# print(count)