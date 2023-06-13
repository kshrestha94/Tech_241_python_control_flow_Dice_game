# Introduction to Python Fundamentals 

`code block using back tick function `

```python
3 back ticks to open box of code
```
```python
################################# variables in python ###########################################   
# A way to store data within a program
# it becomes a reference for that data
# a variables can change
# variable_name = variable_data

a = 1 # int
b = 2
c = 3.5 # float
hi = "my name is kevin!" # string

print(a+b)

# dynamically typed language - Python
# more user-friendly and teachable language and efficient


# in java
# int a = 1;
# in java must determine data type and when you are ending use;
# comment on multiple line control/

# type method code

print(type(a))
# variables can be overwritten as it runs linear

d = 5
print(d)

d = 7
print(d) # python delete the first variable 

# user input

print("what is you name?")
name = input()
print("hi")
print(name)

print("what is you age?")
age = input()
print("kevin is")
print(29)

print("what is your DOB?")
DOB = input()
print("my DOB is")
print(" 02/06/1994 ")

print("what is you address")
address = input()
print("my address is ")
print("London")
```
# Data Types 

```python
######################################### data types ##############################

# numbers int(14) or float(0.5) complex numbers, longs
# strings (characters or text) all characters have specific unicodes.
# boolean (True or False) capitals is important

# operators

# arithmatic operators including modulo % remainder (+ - * /)
# comparison operators ( >, <, ==, !=, >= )

# numerical types

a = 24
b = 16

print(a+b)
print(a-b)
print(a/b)
print(a <b)

float_number = 1.356
int_num = 4

print(type(float_number + int_num))

one_third = 1/3
print( one_third * 3) #  python will always round up

strings "" or ''
single_quotes = 'single'
double_quotes = "double, 'wow!'" # use double quotes when you can include quotation in string

print(single_quotes)
print(double_quotes)

escape_example = 'i said \'wow!\''
print(escape_example)

# string slicing

hi = "hello world2" # space is still a character
print(hi[0:5]) #include [] to reference specific slicing

################################## string methods ##########################

#lenth len()
print(len(hi))

# .strip() to remove white spaces
white_space = "lots of WHITE   space   "
print(len(white_space)) # length
print(len(white_space.strip())) # length removing white spaces

# .lower() or .upper()
print(white_space.lower()) # lower case 
print(white_space.upper()) # upper case 
print(white_space.capitalize())
print(white_space.count("o")) # how many times a character comes on string
print(white_space.replace("space", "new")) # replace word with word

######################### concatenation and casting ############################

x = 2
y = 5.4
z = "this is a string"
zz = "this is also a string"

# concatenation -  adding strings
print(z+ ' ' +zz) #you can add strings but you cant add string and int

# casting

#print(x+y+z) # cannot do because you are mixing int with string
print(str(x) + ' ' +str(y) + ' ' + z) # this example of casting won't add
print(str(x)+str(y) + ' ' + z) # this will but together both strings 

int_string = "6"

print(float(int_string))
print(type(int_string))

# F-string examples 

name = "lasssie"
years = 7
height_cm = 60.2

print(f"{name.upper()} IS {years*7} YEARS OLD IN DOG YEARS")

pi = 3.14159265359
print(f"pie to 3 decimal places: {pi:.3f}")

# percentages
score = 16
max_score = 26

print(f"you scored {score/max_score}")
print(f"you scored {score/max_score:.0%}") #percentage including decimal places .0 or .2 to 2dp

```
# Boolean

```python

########################################### boolean ####################################

a = True
b = False

print(a == b) #False
print(a != b) # True

print(a >= True) # True
print(b >= False) # True

# using keywords

print(True and False) #False
print(False or True) #True
print(True and True) #True

# boolean with data types

hi = "hello world!"

#boolean methods
print(hi.isalpha()) # space and ! to be removed or just alphabetical characters
print(hi.isupper()) # is it upper case ? no therefore, false
print(hi.endswith("!")) #true
print(hi.startswith("h"))# This is True

# the value of 0

x = 0
y = 10

print(bool(x)) # zero is always false - links into binary
print(bool(y))

# value of none or null
# none is not 0, it's not nothing but it's a place holder.

x = None

print(bool(None))
print(x == True)
print(x == None) #not best practice because  == is associated with other factors on boolean

# best practice for checking if something is None
print(x is None) # to check 



```
# Task on casting and concatenation on user detail 

```python
# experiment example task of casting and concatenation

# casting task 

print("what is you address and gender")
address_and_age = input()
print("my address is " + "and gender")
print("London" + ' ' + "male") # casting 

# concatenation task

age = 29
print("what is your name and age")
address_and_age = input()
print("my name is and age")
print("kevin" + ' ' + str(age)) 
# #here i have added the str function to override python to think that the age is a string



```
# code to check Python or GIT version 

```python
Python --version
Git -- version 
```

This concludes the markdown for 12/06/2023.

