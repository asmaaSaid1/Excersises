"""
def fibonacci_numbers(nums):
    x,y=0,1
    for i in range(nums):
        x,y=y,x+y
        yield x
        
def square(nums):
    for num in nums:
        yield num**2
        
def triple(square):
    for num in square:
        yield num**3
    
            
print(sum(triple(square(fibonacci_numbers(10)))))
"""
#program to generate s sequence of even numbers from the list
def even_num(lst):
    a=[]
    for i in lst:
        if i%2==0:
           a.append(i)
    yield a
            
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(next(even_num(lst)))