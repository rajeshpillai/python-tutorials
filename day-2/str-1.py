# Hello Python
s = 'Hello Python'
print (s)
print (s[0])

# Get the length
length = len(s)
print (length)

# Concatenate string
first_name = "Nick"
last_name = "Fury"

full_name = first_name + ' ' + last_name

print (full_name)

# Concatenate number and a string

age = 50

# info = 'The age is ' + age  (throw error)
info = 'The age is ' + str(age)

print (info)

# Multiline string
this_is_big = """I am gonna create a real big string.
Will this work.  Ofcourse.  I trust Python!"""

print(this_is_big)


# Unicode strings
raw = "i ♥ cats"
print (raw)

# Unicode strings
uni = u"i ♥ cats"
print (uni)