#!/usr/bin/env python
# coding: utf-8

# In[1]:


# A simple module, calc.py
def add(x, y):
    return (x+y)

def subtract(x, y):
    return (x-y)


def spam(text):
    print(text, 'spam')
    
    
#Test Assignments
a = 1


# In[2]:


"""
    Exceptions
"""


x = 5 
y = "hello" 
a = [1,2,3]
try: 
    print("Test1")
    print(a[3])
    z = x + y 
    print("Test2")
except TypeError:
    print("Error: cannot add an int and a str")
except IndexError:
    print("Error1")
except:
    print("Error2")

    


# In[3]:


# A simple module, calc.py
#we define two functions, one add and 
another subtract
def add(x, y):
     return (x+y)
def subtract(x, y):
     return (x-y)


# In[9]:


# importing module calc.py
import calc

#print(calc.add(10, 2))

# calc.spam('gumby')



print('-------------------------------')

"""
    Imports Happen Only Once
"""
print(calc.a)  # 1

calc.a = 10   # Change attribute in module
print(calc.a)   #10


import calc   # Just fetches already loaded module

print(calc.a)   # Code wasn't rerun: attribute unchanged

 
print('-------------------------------')

"""
    import Vs. from 
    • import assigns an entire module object to a single name.
    • from assigns one or more names to objects of the same names in another module.
"""


from small import a,b  #copy out a, b into local vars a,b

print(a) #1
print(b)  #[1,2]

a = 20  #changes local a only not the module a
b[0] =15 #changes shared mutbale as list considered a ref obj

print(a)   #20     1
print(b)   #[15,2]

import small   

print(small.a)   #1
print(small.b)   #[15,2]


# In[4]:


#Importing modules in Python Example
#Now, we are importing the calc that we created earlier to perform add operation.

# importing module calc.py
import calc
print(calc.add(10, 2))


# In[ ]:


# we are importing specific sqrt and factorial attributes from the math 
#module.
# importing sqrt() and factorial from the
# module math
from math import sqrt, factorial
# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print(sqrt(16))
print(factorial(6))


# In[6]:


# importing sqrt() and factorial from the
# module math
from math import *
# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print(sqrt(16))
print(factorial(6))


# # Renaming the Python module
We can rename the module while importing it using the keyword.
Syntax: Import Module_name as Alias_name
# In[7]:


# importing sqrt() and factorial from the
# module math
import math as mt
# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print(mt.sqrt(16))
print(mt.factorial(6))


# # Python Built-in modules
# 

# In[8]:


# importing built-in module math
import math
# using square root(sqrt) function contained
# in math module
print(math.sqrt(25))
# using pi function contained in math module
print(math.pi)
# 2 radians = 114.59 degrees
print(math.degrees(2))
# 60 degrees = 1.04 radians
print(math.radians(60))
# Sine of 2 radians
print(math.sin(2))
# Cosine of 0.5 radians
print(math.cos(0.5))
# Tangent of 0.23 radians
print(math.tan(0.23))
# 1 * 2 * 3 * 4 = 24
print(math.factorial(4))
# importing built in module random
import random
# printing random integer between 0 and 5
print(random.randint(0, 5))
# print random floating point number between 0 and 1
print(random.random())
# random number between 0 and 100
print(random.random() * 100)
List = [1, 4, True, 800, "python", 27, "hello"]
# using choice function in random module for choosing
# a random element from a set such as a list
print(random.choice(List))
# importing built in module datetime
import datetime
from datetime import date
import time
# Returns the number of seconds since the
# Unix Epoch, January 1st 1970
print(time.time())
# Converts a number of seconds to a date object
print(date.fromtimestamp(454554))


# ## An abstract class can be considered a blueprint for other classes
It allows you to create a set of methods that must be created within 
any child classes built from the abstract class.

A class that contains one or more abstract methods is called an abstract class. 
An abstract method is a method that has a declaration but does not have an implementation.

By default, Python does not provide abstract classes. Python comes with a module that 
provides the base for defining Abstract Base classes(ABC) and that module name is ABC.
# In[12]:


# Python program showing 
# abstract base class work 

from abc import ABC, abstractmethod 


class Polygon(ABC): 

	@abstractmethod
	def noofsides(self): 
		pass


class Triangle(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 3 sides") 


class Pentagon(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 5 sides") 


class Hexagon(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 6 sides") 


class Quadrilateral(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 4 sides") 


# Driver code 
R = Triangle() 
R.noofsides() 

K = Quadrilateral() 
K.noofsides() 

R = Pentagon() 
R.noofsides() 

K = Hexagon() 
K.noofsides() 


# # Python Exception Handling
Difference between Syntax Error and Exceptions
Syntax Error: As the name suggests this error is caused by the wrong syntax in
the code. It leads to the termination of the program.
Example:
There is a syntax error in the code . The ‘if' statement should be followed by
a colon (:), and the ‘print' statement should be indented to be inside
the ‘if' block
# In[15]:


amount = 10000
if(amount > 2999):
    print("You are eligible to purchase Dsa Self Paced")


# Exceptions are raised when the program is syntactically correct, but
# the code results in an error.

# Here in this code a s we are dividing the ‘marks’ by zero so a error will occur
# known as

# In[16]:


marks = 10000
a = marks / 0
print(a)

Here a ‘TypeError’ is raised as both the datatypes are different which are being
added.
# In[18]:


x = 5
y = "hello"
z = x + y


# # try catch block to resolve it:

# The code attempts to add an integer (‘x') and a string (‘y') together, which is
# not a valid operation, and it will raise a ‘TypeError'. The code used
# a ‘try' and ‘except' block to catch this exception and print an error message.
# 

# In[20]:


x = 5
y = "hello"
try:
     z = x + y
except TypeError:
     print("Error: cannot add an int and a str")

Here we are trying to access the array element whose index is out of
bound and handle the corresponding exception.
# In[21]:


a = [1, 2, 3]
try:
     print ("Second element = %d" %(a[1]))
     print ("Fourth element = %d" %(a[3]))
except:
     print ("An error occurred")


# In the above example, the statements that can cause the error are placed inside
# the try statement (second print statement in our case). The second print
# statement tries to access the fourth element of the list which is not there and
# this throws an exception. This exception is then caught by the except statement.

# # Catching specific exceptions in the Python
# 

# In[22]:


def fun(a):
     if a < 4:
         b = a/(a-3)
     print("Value of b = ", b)
 
try:
     fun(3)
     fun(5)
except ZeroDivisionError:
     print("ZeroDivisionError Occurred and Handled")
except NameError:
     print("NameError Occurred and Handled")


# “ZeroDivisionError Occurred and
# Handled.” The ‘NameError' block is not executed since there are
# no ‘NameError' exceptions in the code.

# # Try with Else Clause
It prints the result if there’s no division
by zero error
# In[26]:


def AbyB(a , b):
    try:
         c = ((a+b) / (a-b))
    except ZeroDivisionError:
         print ("a/b result in 0")
    else:
         print (c)
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)


# # Finally Keyword in Python

# The code attempts to perform integer division by zero, resulting in
# a ZeroDivisionError. It catches the exception and prints “Can’t divide by
# zero.” Regardless of the exception, the finally block is executed and
# prints “This is always executed.”

# In[27]:


try:
     k = 5//0
     print(k)
except ZeroDivisionError:
     print("Can't divide by zero")
finally:
     print('This is always executed')


# # Raising Exception
# 

# In[29]:


try:
    raise NameError("Hi there")
except NameError:
     print ("An exception")
     raise


# In[ ]:




