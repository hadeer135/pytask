#!/usr/bin/env python
# coding: utf-8

# # Solid princibles 
# 1->>> [S] = Single responsibility principle
# In[6]:


# Before applying SRP
class Report:
    def _init_(self, content):
        self.content = content

    def generate_report(self):
        # logic to generate report
        pass

    def save_to_file(self):
        # logic to save report to a file
        pass

# After applying SRP
class Report:
    def _init_(self, content):
        self.content = content

    def generate_report(self):
        # logic to generate report
        pass

class ReportSaver:
    @staticmethod
    def save_to_file(report):
        # logic to save report to a file
        pass

# 2->>>o = open close
# In[7]:


# Before applying OCP
class Rectangle:
    def _init_(self, width, height):
        self.width = width
        self.height = height

class AreaCalculator:
    @staticmethod
    def calculate_area(rectangle):
        return rectangle.width * rectangle.height

# After applying OCP
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def _init_(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# 3->>> l = Liskov Substitution Principle (LSP):
# In[8]:


class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def _init_(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def _init_(self, side):
        super()._init_(side, side)

# Function using LSP
def print_area(shape):
    print(f"Area: {shape.area()}")

# Using LSP with Rectangle and Square
rectangle = Rectangle(3, 4)
square = Square(5)

print_area(rectangle)  # Outputs: Area: 12
print_area(square)     # Outputs: Area: 25

# 4->>>>>  i =  Interface Segregation Principle
# In[9]:


from abc import ABC, abstractmethod



class Shape(ABC):
    @abstractmethod
    def area(self):
        pass



class Rectangle(Shape, ABC):
    @abstractmethod
    def get_width(self):
        pass

    @abstractmethod
    def get_height(self):
        pass



class Square(Rectangle):
    def _init_(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def get_width(self):
        return self.side

    def get_height(self):
        return self.side



class CustomRectangle(Rectangle):
    def _init_(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height



def print_area(shape):
    print(f"Area: {shape.area()}")



def print_rectangle_dimensions(rectangle):
    print(f"Width: {rectangle.get_width()}, Height: {rectangle.get_height()}")




square = Square(5)
custom_rectangle = CustomRectangle(4, 6)


print_area(square)


print_area(custom_rectangle)
print_rectangle_dimensions(custom_rectangle)

# 5 - >>>>> d = Dependency Inversion Principle


class SwitchableDevice:
    def operate(self):
        pass

class LightBulb(SwitchableDevice):
    def operate(self):
        return "LightBulb is ON"  

class Fan(SwitchableDevice):
    def operate(self):
        return "Fan is ON" 
class Switch:
    def _init_(self, device: SwitchableDevice):
        self.device = device

    def operate_device(self):
        return self.device.operate()

light_bulb = LightBulb()
fan = Fan()

switch_for_light = Switch(light_bulb)
print(switch_for_light.operate_device()) 
switch_for_fan = Switch(fan)
print(switch_for_fan.operate_device())

# 5->>>>>  D = Dependency
example of how to apply the dependency inversion principle
# In[10]:


# Define an abstract class for a database connection
class DatabaseConnection:
    def connect(self):
        raise NotImplementedError

    def execute(self, query):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

# Define a concrete class for a MySQL connection
class MySQLConnection(DatabaseConnection):
    def connect(self):
        # Connect to a MySQL database
        print("Connecting to MySQL...")

    def execute(self, query):
        # Execute a query on the MySQL database
        print(f"Executing {query} on MySQL...")

    def close(self):
        # Close the MySQL connection
        print("Closing MySQL connection...")

# Define a concrete class for a MongoDB connection
class MongoDBConnection(DatabaseConnection):
    def connect(self):
        # Connect to a MongoDB database
        print("Connecting to MongoDB...")

    def execute(self, query):
        # Execute a query on the MongoDB database
        print(f"Executing {query} on MongoDB...")

    def close(self):
        # Close the MongoDB connection
        print("Closing MongoDB connection...")

# Define a high-level module that depends on an abstraction
class UserService:
    def __init__(self, db_connection):
        # Use dependency injection to pass the database connection
        self.db_connection = db_connection

    def create_user(self, name, email):
        # Use the database connection to create a user
        self.db_connection.connect()
        self.db_connection.execute(f"INSERT INTO users (name, email) VALUES ('{name}', '{email}')")
        self.db_connection.close()

# Create a MySQL connection object
mysql = MySQLConnection()

# Create a user service object with the MySQL connection
user_service = UserService(mysql)

# Create a user using the user service
user_service.create_user("Alice", "alice@example.com")

# Output:
# Connecting to MySQL...
# Executing INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com') on MySQL...
# Closing MySQL connection...

# Create a MongoDB connection object
mongodb = MongoDBConnection()

# Create another user service object with the MongoDB connection
user_service = UserService(mongodb)

# Create another user using the user service
user_service.create_user("Bob", "bob@example.com")

# Output:
# Connecting to MongoDB...
# Executing INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com') on MongoDB...
# Closing MongoDB connection...


# In[ ]:




