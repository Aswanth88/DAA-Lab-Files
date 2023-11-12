arr = [1,12,11,10,11,1]
newarr=[None,None,None,None,None,None]

def delete_duplicate(arr,newarr):
    m=0
    for i in arr :
        if i not in newarr:
            newarr[m]=i
            m=m+1

delete_duplicate(arr,newarr)
print(newarr)
