#!/usr/bin/env python
# coding: utf-8

# # <font color = 'red'> OBJECT ORIENTED PROGRAMMING </font>

# In[1]:


## Creating and Using a CLASS


# In[2]:


# Creating the DOG Class.


# In[3]:


## Making an object from a class is called instantiation


# In[15]:


class Dog:
    
    """An attempt to create a simple dog"""
    
    def __init__(self,name,age):
        """Initializaing the name and age attributes"""
        self.name = name,
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over.")


# In[ ]:


## Making an instance from a Class

my_dog = Dog("Willie",6)

print(f"{my_dog.name} is my dogs name.")
print(f"My dog is {my_dog.age} years old.")


# In[6]:


## Acessing Attributes


# In[7]:


my_dog.name


# In[10]:


## Calling Methods


# In[11]:


my_dog = Dog('Willie',6)

my_dog.sit()


# In[12]:


my_dog.roll_over()


# In[13]:


## Creating multiple instances


# In[22]:


class Dog:
    
    def __init__(self,name,age):
        self.name = name,
        self.age = age
    
    def sit(self):
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        print(f"{self.age} just rolled over.")



my_dog = Dog('Willie', 6)
your_dog = Dog('Husky', 2)

print(f"My dog's name is{my_dog.name}.")
print(f"My dog's age is {my_dog.age}.")
my_dog.sit()

print(f"\n\tYour dog's name is {your_dog.name}.")
print(f"\tYour dog's age is {your_dog.age}.")
your_dog.sit()


# In[23]:


## Try it yourself exrercises from the book


# In[24]:


## 9-1 - RESTAURANT


# In[43]:


class Cafe:
    
    def __init__(self, cafe_name, coffee_type):
        self.cafe_name = cafe_name
        self.coffee_type = coffee_type
        
    def describe_cafe(self):
        print(f"{self.cafe_name} is the name of the cafe.")
        print(f"{self.coffee_type} made at {self.cafe_name} tastes awesome.")
        
    def open_cafe(self):
        print(f"{self.cafe_name} at Union Street is the first starbucks of San Francisco.")
        print("It is open till 8pm everyday.")


# In[44]:


my_cafe = Cafe('Starbucks','Mocha')


# In[45]:


my_cafe.open_cafe()


# In[50]:


my_cafe.describe_cafe()


# In[51]:


## 9-3 Users


# In[64]:


class User:
    
    def __init__(self,first_name,last_name,location,email):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.location = location.title()
        self.email = email.lower()
    
    def describe_user(self):
        print(f" Full Name: {self.first_name} {self.last_name}")
        print(f" Location: {self.location}")
        print(f" Email: {self.email}")
              
    def greet_user(self):
        print(f" User {self.first_name}, I know everything about you. you have no chance of escapiong fromm me.")
              


# In[65]:


person = User('jim', 'morrison', 'USA', 'jim.morrison@gmail.com')


# In[66]:


person.describe_user()


# In[67]:


person.greet_user()


# In[79]:


## Working with classes and instances


# In[80]:


class Car:
    
    """A simple attempt to represent a car"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_description(self):
        """Return a formatted descriptive name"""
        full_name = f" {self.year} {self.make} {self.model} "
        return full_name.title()
    
my_car  = Car('BMW', '540i Xdrive', 2022)
print(my_car.get_description())


# In[81]:


## Setting a default value for an Attribute


# In[92]:


class Car:
    
    """An attempt to represent a car"""
    
    def __init__(self,make, model, year):
        self.make =  make
        self.model = model
        self.year = year
        self.odometer_reading = 10
        
    def description(self):
        """Return a formatted descriptive name"""
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name.title()

    def read_odometer(self):
        print(f" The odometer reading of this car is {self.odometer_reading} miles.")
        
my_car = Car('BMW', '540i Xdrive', 2022)
print(my_car.description())
my_car.read_odometer()


# In[102]:


## Modifying attribute values


# In[103]:


## Atrributes can be modified in 3 ways

# (1) Directly through the instance.
# (2) Set value through a method.
# (3) Increment value through a method.


# In[104]:


## 1) Modifying an attributes value directly through an instance.


# In[106]:


my_car  =  Car('Mercedes','S-class',2022)
print(my_car.description())

my_car.odometer_reading = 25
my_car.read_odometer()


# In[107]:


## 2) Modifying an attribute value through a Method


# In[114]:


class Car:
    
    """An attempt to represent a car"""
    
    def __init__(self,make, model, year):
        self.make =  make
        self.model = model
        self.year = year
        self.odometer_reading = 10
        
    def description(self):
        """Return a formatted descriptive name"""
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name.title()

    def read_odometer(self):
        print(f" The odometer reading of this car is {self.odometer_reading} miles.")
        
    def update_odometer(self,mileage):
        """Set the odometer to the given value"""
        self.odometer_reading = mileage
        
my_car = Car('BMW', 'M5', 2022)
print(my_car.description())

my_car.update_odometer(25)
print(my_car.read_odometer())


# In[116]:


class Car:
    
    """An attempt to represent a car"""
    
    def __init__(self,make, model, year):
        self.make =  make
        self.model = model
        self.year = year
        self.odometer_reading = 10
        
    def description(self):
        """Return a formatted descriptive name"""
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name.title()

    def read_odometer(self):
        print(f" The odometer reading of this car is {self.odometer_reading} miles.")
        
    def update_odometer(self,mileage):
        """Setting the odometer value to the given value"""
        
        if self.odometer_reading >= mileage:
            self.odometer_reading = mileage
        else:
            print("You cannot rollback the odometer")
        
my_car = Car('BMW', 'M5', 2022)
print(my_car.description())

my_car.update_odometer(25)
print(my_car.read_odometer())


# In[117]:


## Modifying an attributes value through a method


# In[119]:


class Car:
    
    """An attempt to represent a car"""
    
    def __init__(self,make, model, year):
        self.make =  make
        self.model = model
        self.year = year
        self.odometer_reading = 10
        
    def description(self):
        """Return a formatted descriptive name"""
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name.title()

    def read_odometer(self):
        print(f" The odometer reading of this car is {self.odometer_reading} miles.")
        
    def update_odometer(self,mileage):
        """Set the odometer to the given value"""
        self.odometer_reading = mileage
        
    def increment_odometer(self,miles):
        self.odometer_reading += miles
        
my_used_car = Car('BMW', 'M5', 2018)
print(my_car.description())

my_used_car.update_odometer(25)
print(my_car.read_odometer())

my_used_car.increment_odometer(100)
print(my_used_car.read_odometer())


# In[121]:


## Try it yourself Exercises from the Book


# In[122]:


## 9-4 Number Served


# In[171]:


class Cafe:
    
    """An attempt to describe a cafe using a Class"""
    def __init__(self, name, coffee, location):
        self.name = name
        self.coffee = coffee
        self.location  = location
        self.served = 0
        
        
    def describe_cafe(self):
        """Describing the cafe"""
        print(f"\n\t The cafe {self.name} is located at {self.location}.")
        
    def open_timings(self):
        """Timings of the cafe"""
        print(f"The cafe is open 24/7. You are welcome anytime.")
        
    def set_number_served(self, served):
        """Setting a value to the customers served"""
        self.served = served
        print("\nWe have served 10 customers since morning")
        
    def increment_number_served(self, served):
        """Incrementing the value as required"""
        self.served += served
        print("\n\t Oops Sorry, We have served 25 customers since morning.")
        


# In[172]:


se = Cafe('Starbucks', 'Mocha', 'U Village - Seattle, 98105')
se.open_timings()
se.describe_cafe()

se.set_number_served(10)
se.increment_number_served(25)


# In[1]:


## 9-5 Login Attempts


# In[10]:


class User:
    
    def __init__(self,first_name,last_name,location,email):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.location = location.title()
        self.email = email.lower()
    
    def describe_user(self):
        print(f" Full Name: {self.first_name} {self.last_name}")
        print(f" Location: {self.location}")
        print(f" Email: {self.email}")
              
    def greet_user(self):
        print(f" User {self.first_name}, I know everything about you. you have no chance of escapiong fromm me.")
        
              


# In[12]:


person = User('k','lal','seattle','abc@y.com')


# In[13]:


person.greet_user()


# In[14]:


person.describe_user()


# In[25]:


class User:
    
    def __init__(self,first_name,last_name,location,email):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.location = location.title()
        self.email = email.lower()
        self.login_attempts = 0
    
    def describe_user(self):
        print(f" Full Name: {self.first_name} {self.last_name}")
        print(f" Location: {self.location}")
        print(f" Email: {self.email}")
              
    def greet_user(self):
        print(f" User {self.first_name}, I know everything about you. you have no chance of escapiong fromm me.")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0


# In[26]:


eric = User('eric', 'matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()


# In[27]:


print("\nMaking 3 login attempts...")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print(f"  Login attempts: {eric.login_attempts}")

print("Resetting login attempts...")
eric.reset_login_attempts()
print(f"  Login attempts: {eric.login_attempts}")


# In[28]:


## Inheritance


# In[31]:


## Inheritance allows to take attributes and methods of the first class. 
## Original class is called Parent Class and the new class is called Child Class.
## Child class can inherit any or all attributes of parent class.


# In[32]:


## The __init__() Method for a Child Class


# In[3]:


class Car:
    
    """Making a descriptive car class"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    
    def get_descriptive_name(self):
        
        """Getting the description of the cars odometer"""
        
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name
    
    
    def read_odometer(self):        
        print(f" The odometer reading of the car is {self.odometer_reading}.")
        
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot rollback the odometer")
            
    
    def increment_odometer(self,miles):
        self.odometer_reading += miles
        
        

class ElectricCar(Car):
    """Inheritance concept. Lets take the attributes of parent class (Car)."""
    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        
my_tesla = ElectricCar('2022', 'Tesla', 'Model S')
print(my_tesla.get_descriptive_name())


# In[5]:


my_tesla.read_odometer()


# In[7]:


my_tesla.update_odometer(-1)


# In[8]:


my_tesla.increment_odometer(25)


# In[10]:


my_tesla.read_odometer()


# In[11]:


## Defining attributes and Methods for the Child Class


# In[16]:


class Car:
    
    """Making a descriptive car class"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    
    def get_descriptive_name(self):
        
        """Getting the description of the cars odometer"""
        
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name
    
    
    def read_odometer(self):        
        print(f" The odometer reading of the car is {self.odometer_reading}.")
        
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot rollback the odometer")
            
    
    def increment_odometer(self,miles):
        self.odometer_reading += miles
        
        

class ElectricCar(Car):
    """Represents aspects of a car, specific to the electric vehicles"""
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 85
        
    def describe_battery(self):
        print(f"This car has a battery size of {self.battery_size}.")

        
my_tesla = ElectricCar('tesla','model S',2019)
print(my_tesla.get_descriptive_name())
print(my_tesla.describe_battery())


# In[17]:


## Overriding methods from the Parent Class


# In[18]:


class Car:
    
    """Making a descriptive car class"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    
    def get_descriptive_name(self):
        
        """Getting the description of the cars odometer"""
        
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name
    
    
    def read_odometer(self):        
        print(f" The odometer reading of the car is {self.odometer_reading}.")
        
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot rollback the odometer")
            
    
    def increment_odometer(self,miles):
        self.odometer_reading += miles
        
        

class ElectricCar(Car):
    """Represents aspects of a car, specific to the electric vehicles"""
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 85
        
    def describe_battery(self):
        print(f"This car has a battery size of {self.battery_size}.")
        
    def fill_gas_tank(self):
        print("This car does not need a gas tank you idiot")


# In[20]:


my_tesla.fill_gas_tank()


# In[21]:


## Instances as Attributes

## Divide the attrbutes in different class to reduce the length


# In[ ]:


class Car:
    
    """Making a describable car"""
    
    def __init__(self, make, model, year):
        self.make = make
        self.

