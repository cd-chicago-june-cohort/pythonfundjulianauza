x = [19,2,54,-2,7,12,98,32,10,-3,6]
a = x[:len(x)/2]
b = x[len(x)/2:]


print max(x)
#b.append (a)

#print "Updated List : ", b

new = [a] + b
print new