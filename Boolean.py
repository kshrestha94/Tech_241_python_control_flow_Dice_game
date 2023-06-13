# boolean

a = True
b = False

# print(a == b) #False
# print(a != b) # True

# print(a >= True) # True
# print(b >= False) # True

# using key words
#
# print(True and False) #False
# print(False or True) #True
# print(True and True) #True

# boolean with data types

hi = "hello world!"

# #boolean methods
# print(hi.isalpha()) # space and ! to be removed or just alphabetical characters
# print(hi.isupper()) # is it upper case ? no therfore false
# print(hi.endswith("!")) #true
# print(hi.startswith("h"))# This is True

# the value of 0

# x = 0
# y = 10
#
# print(bool(x)) # zero is always false - links into binary
# print(bool(y))

# value of none or null

# non is not 0, its not nothing but its a place holder.

x = None

print(bool(None))
print(x == True)
print(x == None) #not best practice becuase  == is associated with other factors on boolean

# best practice for checking if something is None
print(x is None) # to check



















