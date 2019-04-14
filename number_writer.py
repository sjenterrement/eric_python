import json
number=[1,2,3,4,5,6,7]
filename='C:/Users/ASUS/Desktop/cout.json'
with open(filename,'w') as f_obj:
    json.dump(number,f_obj)
