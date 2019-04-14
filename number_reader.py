import json
filename='C:/Users/ASUS/Desktop/cin.json'
with open(filename,'rb') as f_obj:
    numbers=json.load(f_obj)
print(numbers)
