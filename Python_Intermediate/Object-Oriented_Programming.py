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
