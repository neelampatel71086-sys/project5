class employee:
    def __init__(self,employee_id,name,age,salary):
        self.__employee_id=employee_id
        self.name=name
        self.age=age
        self.__salary=salary
    def get_employee_id(self):
        return self.__employee_id
    def get_salary(self):
        return self.__salary
    def set_employee_id(self,employee_id):
        self.__employee_id=employee_id
    def set_salary(self,salary):
        self.__salary=salary
    def display(self):
        print("employee id:",self.__employee_id)
        print("name:",self.name)
        print("age:",self.age)
        print("salary:",self.__salary)
    def __del__(self):
        print("employee object has been deleted")
class manager(employee):
    def __init__(self,employee_id,name,age,salary,department):
        super().__init__(employee_id,name,age,salary)
        self.department=department
    def display(self):
        super().display()
        print("deparment:",self.department)
class developer(employee):
    def __init__(self,employee_id, name, age,salary,language):
        super().__init__(employee_id, name, age,salary)
        self.language=language
    def display(self):
        super().display()
        print("language:",self.language)
print("manager is a subclass of employee",issubclass(manager,employee))
print("developer is a subclass of a employee",issubclass(developer,employee))
while True:
    print("press 1 for manager class")
    print("press 2 for developer class")
    print("press 3 to knowm about base class")
    print("press 4 for exit")
    
    choice=int(input("entre your choice"))
    if choice==1:
        employee_id=int(input("entre the id"))
        name=input("entre the name")
        age=int(input("entre the age"))
        salary=int(input("entre the salary"))
        department=input("entre the department")
        m=manager(employee_id,name,age,salary,department)
        m.display()
      
    elif choice==2:
        employee_id=int(input("entre the id"))
        name=input("entre the name")
        age=int(input("entre the age"))
        salary=int(input("entre the salary"))
        language=input("entre the language")
        d=developer(employee_id, name, age,salary,language)
        d.display()
       
    elif choice==3:
        employee_id=int(input("entre the id"))
        name=input("entre the name")
        age=int(input("entre the age"))
        salary=int(input("entre the salary"))
        a=employee(employee_id,name,age,salary)
        a.display()
    elif choice==4:
        print("exit")
        break
    else:
        print("invaild choice")
