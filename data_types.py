# data types -
# numbers int(14) or float(0.5) complex numbers, longs
# strings (characters or text) all characters have specific unicodes.
# boolean (True or False) capitals is important

# operators

# arithmatic operators including modulo % remainder (+ - * /)
# comparison operators ( >, <, ==, !=, >= )

# numerical types

# a = 24
# b = 16
#
# print(a+b)
# print(a-b)
# print(a/b)
# print(a <b)
#
# float_number = 1.356
# int_num = 4
#
# print(type(float_number + int_num))
#
# one_third = 1/3
# print( one_third * 3) # round up

# strings "" or ''
# single_quotes = 'single'
# double_quotes = "double, 'wow!'" # use double quotes when you can inc quotation in string
#
# print(single_quotes)
# print(double_quotes)
#
# escape_example = 'i said \'wow!\''
# print(escape_example)

# string slicing

hi = "hello world2" # space is still a character
# print(hi[0:5]) #include [] to reference specific slicing

################################## string methods ##########################

#lenth len()
print(len(hi))

# # .strip() to remove white spaces
# white_space = "lots of WHITE   space   "
# # print(len(white_space)) # length
# # print(len(white_space.strip())) # length removing white spaces
#
# # .lower() or .upper()
# print(white_space.lower())
# print(white_space.upper())
# print(white_space.capitalize())
# print(white_space.count("o")) # how many times a character comes on string
# print(white_space.replace("space", "new")) # replace word with word

######################### concatenation and casting ############################

x = 2
y = 5.4
z = "this is a string"
zz = "this is also a string"

# concatanation -  adding strings
print(z+ ' ' +zz) #you can add strings but you cant add string and int

# casting

#print(x+y+z) # cannot do because you are mixing int with string
print(str(x) + ' ' +str(y) + ' ' + z) # this example of casting wont add
print(str(x)+str(y) + ' ' + z) # this will but together both

int_string = "6"

print(float(int_string))
print(type(int_string))

# F-string

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
print(f"you scored {score/max_score:.0%}") #percentage including decimal places

















