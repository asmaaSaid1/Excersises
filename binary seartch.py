
#binary seartch
"""
key=4
l=[3,1,2,5,4]
hight=l[len(l)-1]
low=l[0]
while low<=hight:
    
    l.sort()
    mid=(hight+low)//2
    if l[mid]==key:
         print("key is in index :" ,mid)
         break
        
    elif key<l[mid]:
         hight=mid-1
    else :
         low=mid+1
       
"""   
"""
#find squareroot of positive number using binary seartch
def binarySearch(key):
    low=0
    hight=key
    while low<=hight:
        
        
        mid=(hight+low)//2
        if(mid==float(key**(0.5))):
             return mid
             break
            
        elif (float(key**(0.5))<mid):
             hight=mid-1
        else :
             low=mid+1


key=float(input("input a positive numpber :"))
print(binarySearch(key))
"""   
        
        