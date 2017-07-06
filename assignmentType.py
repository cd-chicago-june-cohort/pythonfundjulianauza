
l = ['magical unicorns','hello','world']

string="string:"
sum =0
ltypes=[]

for i in l:
    ctype = type(i)
    ltypes.append(ctype)
    if ctype is str:
        string+=str(i)+","
    else:
        sum += i

print string
print sum
#print ltypes

if all(isinstance(i, int) for i in l):
    list_type="integer"
elif all(isinstance(i, str) for i in l):
    list_type="string"
else:
    list_type="mixed"



print "The list you entered is of " + list_type + " type."