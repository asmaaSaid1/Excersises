#reduse

from functools import reduce
num=[1,2,5,7,5]
summ=reduce(lambda x,y:x+y**2,num)
print(summ)