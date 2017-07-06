

# def countOddsNEven():
#    for x in range(1,10):
#         if x % 2 == 0:
#             print x," This is an even number"
#         else:
#             print x," This is an odd number" 

# countOddsNEven()

#Multiply 
# def Multiply(arr,num):
#     newl=[]
#     for x in range(len(arr)):
#         arr[x] *= num
#         newl.append(arr[x])
#     print newl

# Multiply([1,2,3],5)    


#Hacker
def Multiply(arr,num):
    newl=[]
    for x in range(len(arr)):
        arr[x] *= num
        numl=[]
        while arr[x]>0:
            numl.append(1) 
            arr[x]-=1
        newl.append(numl)
    print newl

Multiply([1,2,3],5)   