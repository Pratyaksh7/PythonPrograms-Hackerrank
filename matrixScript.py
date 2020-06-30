def matrix_script():
    first_multiple_input = input().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    
    matrix = []    
    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)
        
    ref = []
    for i in range(m):
        for j in range(n):
            ref.append(matrix[j][i])
            
            
    flag =0        
    for i in range(len(ref)):
        while str.isalnum(ref[i]) and flag ==0 :
            first_alpha_index = ref.index(ref[i])
            flag =1
            break
        
    
    for i in range(len(ref)):
        while str.isalnum(ref[i]) :
            last_alpha_index = ref.index(ref[i])
            break
        
        
    final = []    
    
    
    for i in range(0, first_alpha_index):
        final.append(ref[i])
        
    
    for i in range(first_alpha_index,last_alpha_index+1):
        while str.isalnum(ref[i]):
            final.append(ref[i])
            break
        else:
            while str.isspace(final[-1]):
                break
            else:
                final.append(" ")
        
        
    for i in range(last_alpha_index+1, len(ref)):
        final.append(ref[i])    
        
    print("".join(final))
    
matrix_script()            