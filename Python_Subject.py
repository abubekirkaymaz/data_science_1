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

def welcome(name):
  return "Welcome, " + name

def bye(name):
  return "Goodbye, " + name

def process_user(name, func):
  return func(name)

print(process_user("Alice", welcome))  #Welcome, Alice
print(process_user("Bob", bye)) #Goodbye, Bob

"""
An important concept in Functional Programming is Pure Functions.

A function is called pure if it gives the same result every time you give it the same inputs, and it doesn't affect anything outside of the function. This makes them trustworthy and simpler to understand.
"""
def total(price, count):
  return price * count


"""
The function is impure if it depends on any external state that it modifies or that affects its output. This includes changing variables, or altering input arguments. Such dependencies make the function's behavior unpredictable and dependent on the context in which it's run.
"""
products = ['pen', 'scissors', 'paper']

def add_item(products, item):
  products.append(item)