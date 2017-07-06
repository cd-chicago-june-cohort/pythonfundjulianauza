
# def stars(arr):
#     s=0
    
#     for x in range(len(arr)):
#         s=arr[x]
#         sarr=""
#         while s>0:
#             sarr+="*"
#             s-=1
#         print sarr
        
# stars([1,2,6])


def stars(arr):
    s=0
    for x in range(len(arr)):
        if type(arr[x])==int:
            s=arr[x]
            sarr=""
            while s>0:
                sarr+="*"
                s-=1
            print sarr
        else:
            y=len(arr[x])
            st=""
            while y > 0:
                st+= str.lower(arr[x][:1])
                y-=1
            print st
            
stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
