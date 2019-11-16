# Commonly used string methods

s = " Python is awesome!  "

print (s.lower()) # returns the lowercase version of the string
print (s.upper()) # returns uppercase version of the string
print (s.strip()) # returns a string with whitespace removed from the start and end

# tests if the string chars are in the various character classes
s = "abc"
print (s + ' is alphabet => ' +  str(s.isalpha()))

s = "123"
print (s, " is a digit => ", s.isdigit())

s = " " # note: there is an empty space between the double quotes
print (s, "is a space => ", s.isspace()) 

# tests if the string starts or ends with the given other string
s = "/home/about"
print (s, 'starts with /home => ', s.startswith('/home'))
print (s, 'ends with about => ',s.endswith('about'))

# searches for the given other string (not a regular expression) within s, 
# and returns the first index where it begins or -1 if not found
s = 'Find the needle in the haystack'
print ('The word ""needle"" in the sentence', end='\n *') 
print (s, end = '\n *')
print ("is found at position", s.find("needle"))

# returns a string where all occurrences of 'old' have been replaced by 'new'
s = 'I am getting old again, but yet getting old is a better thing!'
print (s)
print (s.replace('old', 'new')) 

# returns a list of substrings separated by the given delimiter. 
# The delimiter is not a regular expression, it's just text. 
# 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. 
# As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
s = "python,django,flask,numpy"
print("Splitting ", s, "by comma")
print(s.split(',') )


# join() is opposite of split(), joins the elements in the given list 
# together using the string as the delimiter. 
# e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc
s = "****"
list = ["python","is","great"]  #array
print ("Joining the list",list, 'with', s)
print (s.join(list)) 
