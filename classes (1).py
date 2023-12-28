#!/usr/bin/env python
# coding: utf-8

# # OOP

# ### CLASSES 

# Basic class 

# In[2]:


class Customer:
# code for class goes here  pass
    pass
c1 = Customer()  # create an obtect of the class


# #### adding methods to the class

# In[4]:


class Customer:

    def identify(self, name): 
        print("I am Customer " + name)
cust = Customer()
cust.identify("Laura")


# #### Add an attribute to class

# In[16]:


# Define a class called Person
class Person:
    # Define a class attribute called species
    species = "Human"

    # Define the __init__() method
    def __init__(self, name, age):
        # Define two instance attributes called name and age
        self.name = name
        self.age = age

# Create an object of the Person class
p = Person("Alice", 25)

# Print the class and instance attributes
print(p.species) # Human
print(p.name) # Alice
print(p.age) # 25

# Add a new instance attribute called occupation
p.occupation = "Software Engineer"

# Print the new attribute
print(p.occupation) # Software Engineer

Inheritance: This is an example of creating a subclass called Dog that inherits from a superclass called Animal. The Dog class can access and override the attributes and methods of the Animal class, as well as define its own attributes and methods.
# In[17]:


# Define a superclass called Animal
class Animal:
    # Define a class attribute called species
    species = "Animal"

    # Define the __init__() method to initialize the instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Define a method called eat
    def eat(self):
        print(f"{self.name} is eating.")

    # Define a method called sleep
    def sleep(self):
        print(f"{self.name} is sleeping.")

# Define a subclass called Dog that inherits from Animal
class Dog(Animal):
    # Define a class attribute called species
    species = "Dog"

    # Define the __init__() method to initialize the instance attributes
    def __init__(self, name, age, breed):
        # Call the __init__() method of the superclass
        super().__init__(name, age)
        # Define a new instance attribute called breed
        self.breed = breed

    # Define a method called bark
    def bark(self):
        print(f"{self.name} is barking.")

    # Override the eat method of the superclass
    def eat(self):
        print(f"{self.name} is eating dog food.")

# Create an instance of the Dog class
dog = Dog("Max", 3, "Labrador")

# Access the class and instance attributes
print(dog.species) # Dog
print(dog.name) # Max
print(dog.age) # 3
print(dog.breed) # Labrador

# Call the methods of the Dog class and the Animal class
dog.eat() # Max is eating dog food.
dog.sleep() # Max is sleeping.
dog.bark() # Max is barking.

Polymorphism: This is an example of using polymorphism, which is the ability of different objects to respond to the same method in different ways. The print_info() function can take any object that has a name and an info attribute, and print them in a formatted way. The Student and Teacher classes have different implementations of the info attribute, but they can both be passed to the print_info() function.
# In[20]:


# Define a function that can print the name and info of any object
def print_info(obj):
    print(f"Name: {obj.name}")
    print(f"Info: {obj.info}")

# Define a class called Student
class Student:
    # Define the __init__() method to initialize the instance attributes
    def __init__(self, name, grade, courses):
        self.name = name
        self.grade = grade
        self.courses = courses
        # Define an instance attribute called info that returns a string
        self.info = f"A {self.grade} student taking {self.courses} courses."

# Define a class called Teacher
class Teacher:
    # Define the __init__() method to initialize the instance attributes
    def __init__(self, name, subject, salary):
        self.name = name
        self.subject = subject
        self.salary = salary
        # Define an instance attribute called info that returns a string
        self.info = f"A {self.subject} teacher earning {self.salary} per month."

# Create an instance of the Student class
student = Student("Alice", "10th", 5)

# Create an instance of the Teacher class
teacher = Teacher("Bob", "Math", 3000)

# Call the print_info() function with different objects
print_info(student)
# Output:
# Name: Alice
# Info: A 10th student taking 5 courses.

print_info(teacher)
# Output:
# Name: Bob
# Info: A Math teacher earning 3000 per month.

ncapsulation: This is an example of using encapsulation, which is the process of hiding the internal details of an object from the outside world.
# In[25]:


# Define a class called BankAccount
class BankAccount:
    # Define the __init__() method to initialize the instance attributes
    def __init__(self, name, balance, pin):
        self.name = name
        # Define a private attribute called __balance
        self.__balance = balance
        # Define a private attribute called __pin
        self.__pin = pin

    # Define a method called deposit
    def deposit(self, amount):
        # Check if the amount is positive
        if amount > 0:
            # Add the amount to the __balance
            self.__balance += amount
            print(f"Deposited {amount} successfully.")
        else:
            print("Invalid amount.")

    # Define a method called withdraw
    def withdraw(self, amount, pin):
        # Check if the pin is correct
        if pin == self.__pin:
            # Check if the amount is positive and less than or equal to the __balance
            if 0 < amount <= self.__balance:
                # Subtract the amount from the __balance
                self.__balance -= amount
                print(f"Withdrew {amount} successfully.")
            else:
                print("Invalid amount.")
        else:
            print("Wrong pin.")

    # Define a method called check_balance
    def check_balance(self, pin):
        # Check if the pin is correct
        if pin == self.__pin:
            # Return the __balance
            return self.__balance
        else:
            print("Wrong pin.")

# Create an instance of the BankAccount class
account = BankAccount("Alice", 1000, 1234)

# Call the deposit method with a valid amount
account.deposit(500)
# Output: Deposited 500 successfully.

# Call the withdraw method with a valid amount and pin
account.withdraw(200, 1234)
# Output: Withdrew 200 successfully.

# Call the check_balance method with a valid pin
print(account.check_balance(1234))
# Output: 1300

# Try to access the private attributes directly
print(account.balance)
# Output: AttributeError: 'BankAccount' object has no attribute '__balance'
print(account.__pin)
# Output: AttributeError: 'BankAccount' object has no attribute '__pin'


# In[ ]:




