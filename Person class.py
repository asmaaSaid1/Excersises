
from datetime import date
class Person:
  
    def __init__(self,name,age,adress,hours):
        self.name=name
        self.__age=age
        self.adress=adress
        self.hours=hours
        
    def class_type(self):
        return "this is parents calss "


        
class Student(Person):
     def __init__(self,name,age,adress,hours,grade):
            super().__init__(name,age,adress,hours)
            self.grade=grade
            
     def class_type(self):
        return "this is student calss "
    
     
     def new_student(cls,name,birh_year,age,address,hours,grade):
           return cls (name,date.today().year-birh_year,address,hours,grade)
        
s1=Student("Hamza",22,"Mascat",180,[3.1,2.5,2])
p1=Person("Salim",65,"Mascat",180)
print(s1.class_type())
print(p1.class_type())










