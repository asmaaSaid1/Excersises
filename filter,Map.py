"""
#filter 
numbers=[-4,5,6,8,-1,9,-5]
new_list=list(filter(lambda x:x>=0,numbers))
print(new_list)
"""
"""
Strings=['Car','dog','L']
new_list=list(filter(lambda x:x.isupper(),Strings))
print(new_list)"""
"""
#map
names=input("Enter names :")
a=[]
a.append(names)
while names!="":
    names=input("Enter names :")
    a.append(names)
print(a)
new_list=list(map(lambda x:x.upper(),a))
print(new_list)


"""
#reduse
from functools import reduce
num=[1,2,5,7,5]
summ=reduce(lambda x,y:x+y**2,num)
print(summ)
