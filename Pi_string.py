cinfile='C:/Users/ASUS/Desktop/cin.txt'
with open(cinfile) as file_object:
    lines=file_object.readlines()
for line in lines:
    print(line.rstrip())
coutfile='C:/Users/ASUS/Desktop/cout.txt'
"""
    with open(coutfile,'w') as file_object:
    file_object.write("i love programming.\n")
    file_object.write("i love creating new games.\n")
    
"""
    
with open(coutfile,'a') as file_object:
    file_object.write("i also love finding meaning in large datasets.\n")
    file_object.write("i love creating apps that can run in a browser.\n")
    
