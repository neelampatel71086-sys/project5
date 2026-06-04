# project5
Employee Management System using Inheritance in Python
Description

This program demonstrates the concepts of Object-Oriented Programming (OOP) in Python, including:

Classes and Objects
Constructors (__init__)
Destructors (__del__)
Inheritance
Method Overriding
Encapsulation using Private Attributes
Getter and Setter Methods
Menu-Driven Programming

The system manages information about Employees, Managers, and Developers.
Classes Used
1. Employee (Base Class)
Attributes
employee_id (Private)
name
age
salary (Private)
Methods
get_employee_id()
get_salary()
set_employee_id()
set_salary()
display()
__del__()
2. Manager (Derived Class)

Inherits from the Employee class.

Additional Attribute
department
Additional Method
Overrides display() to show department details.
3. Developer (Derived Class)

Inherits from the Employee class.

Additional Attribute
language
Additional Method
Overrides display() to show programming language details.
Features
Check inheritance using issubclass().
Create Manager objects.
Create Developer objects.
Create Employee objects.
Display employee details.
Exit the program through a menu.
Menu Options
Press 1 for Manager Class
Press 2 for Developer Class
Press 3 to Know About Base Class
Press 4 for Exit
Sample Output
manager is a subclass of employee True
developer is a subclass of a employee True

press 1 for manager class
press 2 for developer class
press 3 to know about base class
press 4 for exit

enter your choice: 1
enter the id: 101
enter the name: Rahul
enter the age: 30
enter the salary: 50000
enter the department: HR

employee id: 101
name: Rahul
age: 30
salary: 50000
department: HR
Concepts Demonstrated
Encapsulation

Private attributes:

self.__employee_id
self.__salary
Inheritance
class manager(employee):
class developer(employee):
Method Overriding
def display(self):
    super().display()
Destructor
def __del__(self):
    print("employee object has been deleted")
Requirements
Python 3.x
Author

Niyati Patel
