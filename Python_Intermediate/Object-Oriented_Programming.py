"""
#-----------------------------------------------------------------------------------------------------------------------------
#Introduction to OOP

#To add attributes to a class, you must define the __init__ method. This method's first parameter is always self, which represents the instance of the class. Following self, you specify the attributes you wish to include. Then, inside the function, you assign values to the initialized object's attributes, setting their initial state.

#In addition to attributes, you can add custom behaviors to a class by defining functions within it. These functions, known as methods, should include the 'self' parameter to interact with the class instance. You can call these methods using the dot . notation, similar to how you access attributes.

#The main difference between functions and methods is that functions are independent and can be called on their own, while methods are associated with a class and can be called only with its instance. This means that you can't call a method without having the instance of a class where that method is defined.

class Car:
  def __init__(self, brand, color):
    self.brand = brand
    self.color = color
  
  def honk(self):
    print("Beep beep")


my_car = Car("BMW", "red")

print(my_car)
print(my_car.brand)
print(my_car.color)

my_car.honk()

#Everything in Python, including functions, is an object. For instance, integers are instances of the int class, and functions are instances of the function class, among others. This object-oriented nature underlies Python's flexibility and power.

#function
def greet():
  print("Welcome!")

#list
prices = [55, 68, 77, 36]

#data types
x = 5
city = "London"
is_open = True

print(type(greet)) #<class 'function'>
print(type(prices)) #<class 'list'>
print(type(x)) #<class 'int'>
print(type(city)) #<class 'str'>
print(type(is_open)) #<class 'bool'>

"""

"""
#-----------------------------------------------------------------------------------------------------------------------------
#Inheritance

class Animal:
  def __init__(self, name):
    self.name = name
  
  def move(self):
    print("Moving")

# Inherits from Animal class
class Dog(Animal):
  # Specific behavior
  def bark(self):
    print("Woof!")
    
# Creating an instance
my_dog = Dog("Bob")

# Inherited attribute and behavior
print(my_dog.name)
my_dog.move()

# Specific behavior
my_dog.bark()

#A class from which others are inherited is known as a superclass or parent class. Conversely, a class that inherits from another class is referred to as a subclass or child class.


#What if we want to not only inherit attributes but also add specific ones to a child class? In this case, we define an __init__ method in the child class. Use super().__init__() to inherit attributes from the parent class, and then define any additional attributes as usual.

#parent class
class Animal:
  def __init__(self, name):
    self.name = name
  
  def move(self):
    print("Moving")

#child class
class Dog(Animal):
  def __init__(self, name, breed, age):
    # Initialize attributes of the superclass
    super().__init__(name)
    # Additional attributes specific to Dog
    self.breed = breed
    self.age = age

  def bark(self):
    print("Woof!")


my_dog = Dog("Jax", "Bulldog", 5)
#inherited attribute
print(my_dog.name)

#Additional attributes
print(my_dog.breed)
print(my_dog.age)


#You can define methods with the same name in both parent and child classes, but they can perform different operations. This is known as method overriding. For instance, consider the Animal class with a sound method. The Dog and Cat child classes inherit the sound method from Animal but override it to suit their specific needs.
# Parent class
class Animal:
  def __init__(self, name):
    self.name = name

  # Generic sound method for any animal
  def sound(self):
    print("Making a sound")

# Child class Dog
class Dog(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age
  
  # Overridden sound method for Dog
  def sound(self):
    print("Woof!")

# Child class Cat
class Cat(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age

  # Overridden sound method for Cat
  def sound(self):
    print("Meow!")

# Creating instances
my_dog = Dog("Jax", "Bulldog", 5)
my_cat = Cat("Lily", "Ragdoll", 2)

# Using overridden methods
my_dog.sound()
my_cat.sound()



#You can use the super()  function if you want to call a method from the parent class while overriding it. This is useful when you want to add some functionality to the child class method without changing the original one.
# Parent class
class Animal:
  def __init__(self, name):
    self.name = name

  # Generic sound method for any animal
  def sound(self):
    print("Making a sound")

# Child class Dog
class Dog(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age
  
  # Overridden sound method for Dog
  def sound(self):
    # Call the sound method from Animal
    super().sound()
    # Additional functionality for Dog
    print("Woof!")

# Creating an instance of Dog
my_dog = Dog("Jax", "Bulldog", 5)

# Calling the overridden sound method
my_dog.sound()

#Method overriding is a demonstration of another key concept in OOP - polymorphism. Polymorphism lets objects use methods in their own way, even if they share the same name. In this example, even though each animal in the animals list may be of a different subclass, the code can call sound() on each without needing to know its specific type.
# Parent class
class Animal:
  def __init__(self, name):
    self.name = name

  # Generic sound method for any animal
  def sound(self):
    print("Making a sound")

# Child class Dog
class Dog(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age
  
  # Overridden sound method for Dog
  def sound(self):
    print("Woof!")

# Child class Cat
class Cat(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age

  # Overridden sound method for Cat
  def sound(self):
    print("Meow!")

# Creating instances
my_dog = Dog("Jax", "Bulldog", 5)
my_cat = Cat("Lily", "Ragdoll", 2)

animals = [my_dog, my_cat]

for animal in animals:
  animal.sound()

"""

#-----------------------------------------------------------------------------------------------------------------------------
#Data Hiding

#Consider the Car class provided below. After creating an instance of this class, you can access and modify its attributes, as well as call its methods.

# class Car:
#   def __init__(self, model, year, odometer):
#     self.model = model
#     self.year = year
#     self.odometer = odometer

#   def describe_car(self):
#     print(self.year, self.model)

#   def read_odometer(self):
#     print("Odometer:", self.odometer, "miles")

# my_car = Car('Audi', 2020, 15000)

# my_car.describe_car()
# my_car.read_odometer()

# #changing a value of the attribute
# my_car.odometer = 20000

# my_car.read_odometer()

#In programming, sometimes it's crucial to 'protect' certain class attributes and methods from being accessed outside the class. This is called data hiding and ensures the integrity and security of the data, preventing unintended or harmful modifications.
#In Python, data hiding has two levels. The first involves prefixing an attribute with a single underscore _, signaling it's meant for internal use and should be viewed as 'protected'.
#Attributes with a single underscore are accessible but considered protected by convention, signaling they're for internal use and should be accessed cautiously outside the class.To access a protected attribute outside of the class, use the single underscore prefix, as that's part of the attribute's name.

# class Car:
#   def __init__(self, model, year, odometer):
#     self.model = model
#     self.year = year
#     # Making the odometer attribute 'protected'
#     self._odometer = odometer  

#   def describe_car(self):
#     print(self.year, self.model)

#   def read_odometer(self):
#     print("Odometer:", self._odometer, "miles")

# my_car = Car('Audi', 2020, 15000)

# my_car.describe_car()
# my_car.read_odometer()

# #accessing the protected attribute
# print(my_car._odometer)

#The next level of data hiding involves making an attribute private. This is achieved by prefixing the attribute name with two underscores (e.g., __attribute). In this case, unlike protected attributes, this is not just a convention - it limits its access outside the class through name mangling, enhancing data protection and encapsulation. This method is used for sensitive or internal data, strongly discouraging external access.

# class Car:
#   def __init__(self, model, year, odometer):
#     self.model = model
#     self.year = year
#     # Making the odometer attribute 'private'
#     self.__odometer = odometer

# Accessing a private attribute with double underscores from outside the class causes an error, but it's accessible within class methods. This demonstrates encapsulation, protecting sensitive data from external access and ensuring it's only reachable via specific methods, aligning with object-oriented programming principles.

# class Car:
#   def __init__(self, model, year, odometer):
#     self.model = model
#     self.year = year
#     # Making the odometer attribute 'private'
#     self.__odometer = odometer  

#   def describe_car(self):
#     print(self.year, self.model)

#   def read_odometer(self):
#     print("Odometer:", self.__odometer, "miles")

# my_car = Car('Audi', 2020, 15000)

# #accessing the attribute within method
# my_car.read_odometer()

# #error
# # print(my_car.__odometer)


#Accessing a private attribute directly from outside its class is generally discouraged in Python. However, Python employs name mangling for private attributes, which means you can access them using a specific naming convention from outside the class if necessary.However, this approach should be used sparingly, as it bypasses the encapsulation principles intended by making the attribute private. 

# class Car:
#   def __init__(self, model, year, odometer):
#     self.model = model
#     self.year = year
#     # Making the odometer attribute 'private'
#     self.__odometer = odometer  

#   def describe_car(self):
#     print(self.year, self.model)

#   def read_odometer(self):
#     print("Odometer:", self.__odometer, "miles")

# my_car = Car('Audi', 2020, 15000)

# #accesing using name mangling
# print(my_car._Car__odometer)

# You can also designate methods as protected or private, following the same convention as with attributes. Protected methods are prefixed with a single underscore and can be accessed within the class and its subclasses. However, private methods, marked by a double underscore, cannot be directly accessed from outside the class.
class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'private'
    self.__odometer = odometer  

  def _describe_car(self):  # Making the describe_car method 'protected'
    print(self.year, self.model)

  def __read_odometer(self):  # Making the read_odometer method 'private'
    print("Odometer:", self.__odometer, "miles")


my_car = Car('Audi', 2020, 15000)

#accessing protected method
my_car._describe_car()

#error when accessing a privet method
# my_car.__read_odometer()