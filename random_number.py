#create random number
import random
import string
str_a = "abc"
#use abc to glue every number
s2= str_a.join([str(random.randint(0,9)) for _ in range(3)])
print(s2)

#create a number 3 times and translate into type str
print ("".join([str(random.randint(2,6)) for _ in range(3)]))
