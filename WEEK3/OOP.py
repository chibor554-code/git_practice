#creating a class

class Dog:
    """A simple Dog class."""
    # Class attribute - shard by all dogs
    species = "canis familiaris"
    
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age
    
    def __init__(self, name, age):
        self.name = name
        self.age = age # this is an attribute
        
        
    def bark(self):
        return f"{self.name} says woof!"
    
    def description(self):
        return f"{self.name} is {self.age} years old"
    
# creat object instance from the class
rex = Dog("Rex",7) # object
    
print(rex.name)
print(rex.age)
    
print(rex.description())
print(rex.bark())

print(Dog.species)
