"""
# Strings are immutable
word = "car"
#word[2] = "t" #error

# Lists are mutable
words = ["car", "dog", "bird"]
words[0] = "cat"
print(words)

"""
"""
Python'daki sequence (dizi), sirali ve erişilebilir veri koleksiyonlarini ifade eder. Tüm sequence'lar şu ortak özelliklere sahiptir:

İçerikleri siraya göre düzenlenmiştir (ordered).
Her bir elemanina indeksler (index) kullanilarak erişilebilir.
Bazi operasyonlari (örneğin dilimleme, yineleme gibi) desteklerler.


years = [2002, 2008, 1999]
years[1] = 2007
for year in years:
  print(year)

"""
#--------Python Intermadiate--------#
#--------Introduction to Functional Programming---------#

"""
In Python, functions that operate with other functions — that is, take another function as an argument or return a function -  are called Higher-Order Functions. They are particularly useful for processing various functions and returning specific results.
"""

# def welcome(name):
#   return "Welcome, " + name

# def bye(name):
#   return "Goodbye, " + name

# def process_user(name, func):
#   return func(name)

# print(process_user("Alice", welcome))  #Welcome, Alice
# print(process_user("Bob", bye)) #Goodbye, Bob

"""
An important concept in Functional Programming is Pure Functions.

A function is called pure if it gives the same result every time you give it the same inputs, and it doesn't affect anything outside of the function. This makes them trustworthy and simpler to understand.
"""
# def total(price, count):
#   return price * count


"""
The function is impure if it depends on any external state that it modifies or that affects its output. This includes changing variables, or altering input arguments. Such dependencies make the function's behavior unpredictable and dependent on the context in which it's run.
"""
# products = ['pen', 'scissors', 'paper']

# def add_item(products, item):
#   products.append(item)

#*************************************************************************************
#***Lambda Expressions***
#*************************************************************************************

"""Lambda expressions are functions without a name that are quick to create and use. They are written in just one line using the lambda keyword and are often used for small, simple tasks. Lambda expressions are called anonymous functions. Don't need name"""

# def greet (name): 
#   return "Welcome, " + name

# print(greet('Ali')) #Welcome, Ali


# greet = lambda name: "Welcome, " + name

# print(greet("Bob"))

# discount = lambda price: price * 0.9 
# print(discount(100)) #90.0


"""You can provide arguments to lambda expressions on-the-fly by adding them in parentheses immediately after the lambda function. The lambda expression should be also enclosed in parentheses."""
# res = (lambda x, y: x + y) (2, 3)
# print(res) #5



"""function inside another function. Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:"""
# def mult(n):
#   return lambda a : a * n

# doubler = mult(2)
# tripler = mult(3)

# print(doubler(5)) #10
# print(tripler(5)) #15



#*************************************************************************************
#***map and filter***
#*************************************************************************************

# #List of names in various cases
# names = ["alice", "bob", "CHARLIE", "dEborah"]

# # Function to capitalize each name
# def capitalize(name):
#   return name.capitalize()

# # Using map() to apply the capitalization to each name
# capitalized = map(capitalize, names)

# # Converting map object to a list
# capitalized = list(capitalized)

# print(capitalized)

# prices = [25.99, 14.50, 8.75, 19.95]
# def discount(price):
#   discounted_price = price * 0.9
#   return discounted_price

# discounted_prices = list(map(discount, prices))
# print(discounted_prices)

# numbers = [1, 2, 3]
# doubled = list(map(lambda x: x*2, numbers))
# print(doubled)


#The filter() function, just like the map() function, takes in a function and an iterable as arguments. The key purpose of filter() is to apply a condition specified in the provided function to each item in the iterable and return only those for which the function evaluates to True.

# products = ["Table", "Sofa", "Cushion", "Bookshelf", "Vase"]
# # Filters products with name length equal to 4
# filtered_prod = list(filter(lambda name: len(name) == 4, products))
# print(filtered_prod)

# products = {'Table': 110, 'Sofa': 120, 'Chair': 45, 'Lamp': 70}
# #filtering products with prices less than 90
# filtered_products = dict(filter(lambda item: item[1] < 90, products.items()))
# print(filtered_products)


# names = ["John", "Emma", "Jake", "Rachel", "James"]
# filtered = list(filter(lambda name: name[0] == 'J', names))
# print(filtered)


#*************************************************************************************
#***args and kwargs***
#*************************************************************************************

#*args receives arguments as a tuple, which can be used inside the function.
#You need to use the unpacking operator * before args. This operator informs Python that the argument is an iterable and should be unpacked to receive its values as individual arguments.
#Note that args is just a name. You’re not required to use the name args. You can choose any name that you prefer.
#When defining a function with both regular arguments and *args, the regular arguments must come before *args in the function definition.
#Extra:The first line of the function definition, which includes the function name and its parameters, is called function signature.
#Python also allows you to pass keyword arguments using **kwargs. In this case, **kwargs receives arguments in the form of a dictionary, consisting of key:value pairs.
#The ** operator in Python is used to unpack dictionaries into arguments. It enables a function to accept an arbitrary number of keyword arguments, converting these arguments into a dictionary of key:value pairs.
#In a function definition, the order of arguments is important. First, regular arguments are listed, followed by *args for positional arguments, and finally **kwargs for keyword arguments.



# #**kwargs is a dictionary
# def display_info(**kwargs):
# #kwargs.items() returns the key:valie pairs
#   for key, value in kwargs.items():
#     print(key, ":", value)

# display_info(name="Alice", age=30, city="New York")


#*************************************************************************************
#***Decorators***
#*************************************************************************************

# #In Python, functions can be nested. This means you can define a function inside another function's body.
# #outer function
# def outer_function():
#   print("Hello from the outer function")
#   #inner function
#   def inner_function():
#     print("Hello from the inner function")
#   inner_function()

# outer_function()


# #You can also return the result of the nested function directly from within the body of the parent function.
# def greet(name):
#   print("Hey", name)

#   def account():
#     return "Your account is created!"

#   message = account()
#   return message

# print(greet("Bob"))



# def order():
#   def prepare():
#     return "Your meal is being prepared!"
#   status = prepare()
#   return status

# print(order())


# #Bir mesaj üreten bir fonksiyonunuz olduğunu düşünün. Amacınız, bu orijinal fonksiyonu bir argüman olarak alan ve orijinal fonksiyonun kodunu değiştirmeden orijinal mesajı büyük harfe dönüştüren başka bir fonksiyon oluşturmaktır. Bu fonksiyonlar dekoratör olarak bilinir. Aşağıdaki kodda, uppercase() fonksiyonu bir dekoratör olarak hareket eder ve wrapper() fonksiyonu greet() fonksiyonunun değiştirilmiş (veya dekore edilmiş) versiyonunu temsil eder.
# def greet():
#     return "Welcome!"

# #takes a function as an argument
# def uppercase(func):
#   #wrapper function to keep the
#   #original function code unchanged
#   def wrapper():
#     orig_message = func()
#     modified_message = orig_message.upper()
#     return modified_message
#   return wrapper

# greet_upper = uppercase(greet)
# print(greet_upper())


# #You can apply a decorator to a function using the @ sign. It improves the code readability and provides a clean separation between the function and its decoration. When a function with a decorator is called, it automatically includes the behavior defined in the decorator.
# def uppercase(func):
#   def wrapper():
#     orig_message = func()
#     modified_message = orig_message.upper()
#     return modified_message
#   return wrapper

# @uppercase
# def greet():
#     return "Welcome!"

# # Using the decorated function
# print(greet())


# #Decorators are a powerful feature, offering a concise, readable, and efficient way to enhance the functionality of existing functions.You can apply the same decorator to several different functions:
# def stock_status_decorator(func):
#   def wrapper(item):
#     result = func(item)
#     print(result, ": stock status for", item)
#     return result
#   return wrapper

# @stock_status_decorator #restock_item = stock_status_decorator(restock_item)
# def restock_item(item):
#     return "Restocked"

# @stock_status_decorator #sell_item = stock_status_decorator(sell_item)
# def sell_item(item):
#     return "Sold"

# print(restock_item("Laptop"))
# print(sell_item("Smartphone"))
