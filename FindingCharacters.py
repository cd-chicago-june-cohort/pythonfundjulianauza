
s = ['hello','world','my','name','is','Anna']
new_list=[]

for i in s:
    for char in i:
        if char == "o":
            new_list.append(i)

print new_list