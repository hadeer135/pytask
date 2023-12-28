#!/usr/bin/env python
# coding: utf-8

# In[1]:


#A variable assigns a name to a value#
message = "Hello, world!"
n = 42
e = 2.71
# note we can print variables:
print(n) 
# yields 42
# note: everything after pound sign is a comment


# In[2]:


#Almost always preferred to use variables over values:
length = 4.2
height = 3.5
area = length * height
prim = 2 * (length + height)
print(area, prim)


# In[3]:


#define variable type in Python
type(1) # => <class ‘int’> 
type(1.) # => <class ‘flot’> 
type("hello") # => <class ‘str’>  
type('Hello') # => <class ‘str’>  
type(None) # => <class ‘NoneType’>


# In[4]:


# for loop
for i in range(5): 
    print (i**2)
# 0 1 4 9 16


# In[34]:


# this code will print "the statement is true" if the  number is greater than 0 and will print "the statement is false" if the  number is less than 0 
number = -5
if number > 0:
    print("the statement is true")
else:
    print("the statement is false")


# In[6]:


#range(start, end, step)
for i in range(1, 10, 2):
    print (i) 
# 1 3 5 7 9


# In[10]:


#while loop
i = e
i < 20 
print(i**2) 
i += i**2
# a += b is short for a = a + b  # 1 4 36 1764


# In[38]:


#break statement
max_n = 10
for n in range(2, max_n):
    for x in range(2, n):
        if n % x == 0:
            # n divisible by x
            print(n, ' equals ', x, ' * ', n/x)
            break
        else:
            # n is a prime number
            print(n, ' is a prime number')
              # executed if no break in for loop
# loop fell through without finding a factor  print n, ‘is a prime number’


# In[33]:


traffic_light='green'
if traffic_light == 'green' :  
    pass # to implement later
else:
    stop()


# # Functions
# 

# In[40]:


h=10
w=10
def Rec_area(h, w): 
    area = h * w
    return area



# In[48]:


def loop():
    for x in range(10):  
        print (x)
            
        if x == 3:
            return


# In[60]:


def function1(x):  
    def function11(y):
        print(y + 2)  
        return y + 2
    a= 3 * function11(x) # calling the inner function inside the scope of the outer
    return a

# call the function
result = function1(2)
print(result)


##################################################################################

# return the inner function itself
def function1(x):  
    def function11(y):
        print(y + 2)  
        return y + 2
    return function11 # return the inner function 

# call the outer function and assign the inner function to a variable
b = function1(2)
print(b(2.5)) # 4.5

 


# In[56]:


#function returns other function
def twice (func ,x):
    return func(func(x))
def mul(x):
    return x**2
out = twice(mul ,2)
print (out)


# # Global Keyword

# In[68]:


#Global Variable 
x=10
def change ():
    global x
x=x+5
print(x)
change()
print(x)


# # Shallow and Deep copying
# 

# In[72]:


#share the same refrence to the nested elemnts
import copy

# create a nested list
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# make a shallow copy
new_list = copy.copy(old_list)

# modify the new list
new_list[0][0] = 0

# print both lists
print("Old list:", old_list)
print("New list:", new_list)



# In[71]:


#have independent copies of the nested elemnts 
import copy

# create a nested list
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# make a deep copy
new_list = copy.deepcopy(old_list)

# modify the new list
new_list[0][0] = 0

# print both lists
print("Old list:", old_list)
print("New list:", new_list)


# # Abstract method

# In[73]:


from abc import ABC, abstractmethod

# create an ABC
class Vehicle(ABC):

    # create an abstract method
    @abstractmethod
    def start(self):
        pass

    # create another abstract method
    @abstractmethod
    def stop(self):
        pass

# create a subclass that inherits from the ABC
class Car(Vehicle):

    # override the abstract methods
    def start(self):
        # print the action of the car
        print("The car starts with a key")

    def stop(self):
        # print the action of the car
        print("The car stops with a brake")

    # define the constructor
    def __init__(self, model, color):
        self.model = model
        self.color = color

# create another subclass that inherits from the ABC
class Bike(Vehicle):

    # override the abstract methods
    def start(self):
        # print the action of the bike
        print("The bike starts with a button")

    def stop(self):
        # print the action of the bike
        print("The bike stops with a pedal")

    # define the constructor
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

# create another subclass that inherits from the ABC
class Bus(Vehicle):

    # override the abstract methods
    def start(self):
        # print the action of the bus
        print("The bus starts with a switch")

    def stop(self):
        # print the action of the bus
        print("The bus stops with a lever")

    # define the constructor
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity

# create an instance of the Car subclass
c = Car("Toyota", "Red")
# call the start and stop methods and print the result
c.start() # The car starts with a key
c.stop() # The car stops with a brake

# create an instance of the Bike subclass
b = Bike("Honda", 100)
# call the start and stop methods and print the result
b.start() # The bike starts with a button
b.stop() # The bike stops with a pedal

# create an instance of the Bus subclass
bu = Bus(101, 50)
# call the start and stop methods and print the result
bu.start() # The bus starts with a switch
bu.stop() # The bus stops with a lever


# # Default Argument  

# In[78]:


def func(x ,a=1,b=2):
    return x+a-b
print (func(1)) #return 0
print (func(1,2)) #return 1
print (func(1,2,1)) #return 2
print (func(1,b=3)) #return -1


# # Lists: slicing and adding

# In[82]:


Mylist = [5, 2.3, 'hello']
Mysecondlist = ['a', 3]

Concatenated = Mylist+ Mysecondlist
print (Concatenated)
# [5, 2.3, ‘hello’, ‘a’, 3]

print (Mylist * 2)
# [5, 2.3, ‘hello’, 5, 2.3, ‘hello’]  print 2 * Mylist


# # Functions modify lists

# In[84]:


def modify_items(L):
    L[0] = 0
A=[1,2,3]
print(A)
modify_items(A)
print(A)


# # Loop over list elements

# In[85]:


someIntegers = [1, 3, 10]

for i in someIntegers: 
    print (i)


# In[86]:


Mylist = [1, 5, 10]

for index, elem in enumerate(Mylist):  
    print ({0}),{1},).format(index, elem)


# # List comprehension

# In[87]:


ints = [1, 3, 10]
[i * 2 for i in ints]  # [2, 6, 20]
[[i, j] for i in ints for j in ints if i != j]


# # Tuples
# #### Unlike lists, we cannot change elements

# In[90]:


myTuple = (1, 2, 3) 
print (myTuple[1])
# 2
print (myTuple[1:3]) 
# (2, 3)


# # Packaging and unpacking

# In[91]:


#Packaging: we can use the asterisk (*) operator to pack all the arguments of a function into a tuple
def add(*args):
    # args is a tuple of all the arguments
    total = 0
    for num in args:
        total += num
    return total

print(add(1, 2, 3)) # prints 6
print(add(10, 20, 30, 40)) # prints 100


# In[93]:


#Functions with multiple return values
def simple_function(): 
    return 0, 1, 2
print (simple_function()) 
# (0, 1, 2)


# # Dictionaries
# #### No duplicate keys, old value gets overwritten instead

# In[ ]:





# # Sets 

# In[ ]:





# # Set comprehensions

# In[ ]:





# # String: Split , join

# In[ ]:





# In[ ]:




