class Employee:
    def __init__(self,Id,name,salary,department):
        
        self.Id=Id
        self.name=name
        self.salary=salary
        self.department=department
    def salary_(self,salary,hour_work):
        overtime=hour_work-50
        if hour_work> 50:
             self.salary=salary+overtime
        else:
             self.salary=salary
            
        
    def department(self,new_department):
        self.department=new_department
        
    def print_employee(self):
      return f" {self.name}, {self.Id} ,{self.salary}, {self.department}"
    
p1=Employee("ADAMS","E7499",5000,"ACCOUNTING")
print(p1.print_employee())

p1.department="Statistics"

print(p1.print_employee())

p1.salary_(600,70)
print(p1.salary)


    
    