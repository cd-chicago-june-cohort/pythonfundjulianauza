name = ["Anna", "Eli", "Pariece", "Brendan"]
animal = ["horse", "cat", "spider", "giraffe"]

def make_dict(arr1, arr2):
    new_dict = dict.fromkeys(arr1,arr2)
#     val=""
#     key=""
#     for x in arr1:
#         key = x
#     for y in arr2:
#         val = y 
#     new_dict[key]=val
    return new_dict

make_dict(name,animal)