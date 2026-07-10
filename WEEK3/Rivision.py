# # creat a class 
# class Student_Profile:
#     tech_hub = "Learn Factory Nigeria" # class attribute
#     def __init__(self, first_name, last_name, age):
        
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
        
#     def print_profile(self):
#         return f"Name: {self.first_name} {self.last_name},age: {self.age}"
# Ikenna = Student_Profile("Ikenna", "Chibor", 50)
# print(Ikenna.first_name, Ikenna.last_name, Ikenna.age)
# print(Ikenna.print_profile())
# print(Ikenna.tech_hub)



# Class Attributes vs Instance Attributes 
class Employee: 
    company = "TechRise Inc"   # class attribute — shared by ALL employees 
    raise_amount = 1.05 
    
    def __init__(self, name, salary): 
        self.name   = name     # instance attribute — unique per employee 
        self.salary = salary   # instance attribute — unique per employee 
        
    def apply_raise(self): 
        self.salary = int(self.salary * self.raise_amount) 
        return self.salary
emp1 = Employee("Ada", 50000) 
emp2 = Employee("Kemi", 60000) 

# print(emp1.company)    # TechRise Inc  (from class) 
# print(emp1.name)       # Ada           (from instance) 
# Changing a class attribute affects ALL instances 

# Employee.company = "TechRise Global" 
# print(emp1.company)    # TechRise Global 
# print(emp2.company)    # TechRise Global 
# # Setting on an instance creates a COPY just for that instance 

# emp1.company = "Different Co" 
# print(emp1.company)    # Different Co 
# print(emp2.company)    # TechRise Global  (unchanged)

# print(emp1.apply_raise())
# print(emp2.apply_raise())


# # PARENT class (base class) 
# class Animal: 
#     def __init__(self, name): 
#         self.name = name 
#     def speak(self): 
#         raise NotImplementedError("Every animal must implement speak()")
    
    
#     # CHILD classes — inherit from Animal 
# class Dog(Animal):            # (Animal) = inherit from Animal 
#     def speak(self):          # overrides the parent method 
#         return f"{self.name} says Woof!" 
# class Cat(Animal): 
#     def speak(self): 
#         return f"{self.name} says Meow!"
    
# dog1 = Dog("German Serpherd")
# print(dog1.speak())
# cat1 = Cat("black cat")
# print(cat1.speak())

# class Admin(Employee):
#     raise_amount = 1.3
#     def raise_amount(self):
#         self.salary = int(self.salary * self.raise_amount)
#         return self.raise_amount
# emp1 = Employee("Ikenna", 50000)  
# print(emp1.apply_raise())
# #this work is not completed


# class Person: 
#     def __init__(self, name, age): 
#         self.name = name 
#         self.age  = age 
        
#     def greet(self): 
#         return f"Hello, I am {self.name}." 
    
# class Student(Person):         # inherits from Person 
#     def __init__(self, name, age, course): 
#         super().__init__(name, age)   # call Person's __init__ first 
#         self.course = course          # then add our own extra data 
        
#     def study(self): 
#         return f"{self.name} is studying {self.course}." 
    
# ada = Student("Ada", 25, "Enterprise Python") 
# print(ada.greet())    # Hello, I am Ada.     (inherited from Person) 
# print(ada.study())    # Ada is studying Enterprise Python. 



#  Polymorphism — Same Interface, Different Behaviour
class Shape: 
    def area(self): 
        pass   # to be overridden by child classes 
    
class Rectangle(Shape): 
    def __init__(self, width, height): 
        self.width  = width 
        self.height = height 
    def area(self): 
        return self.width * self.height 
    
class Circle(Shape): 
    def __init__(self, radius): 
        self.radius = radius 
    def area(self): 
        return 3.14159 * self.radius ** 2 
    
# Polymorphism in action — same function, works with ANY Shape 
def print_area(shape): 
    print(f"Area: {"shape".area():.2f}") 
shapes = [Rectangle(5, 4), Circle(3), Rectangle(10, 2)] 
for shape in shapes: 
    print_area(shape)    # works for all — each responds differently 