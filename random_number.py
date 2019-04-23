#create random number
import random
import string
str_a = "abc"
#use abc to glue every number
s2= str_a.join([str(random.randint(0,9)) for _ in range(3)])
print(s2)

#create a number 3 times and translate into type str
print ("".join([str(random.randint(2,6)) for _ in range(3)]))
#create a random word with 8 letters 
print("".join([chr(random.randint(97,122)) for _ in range(8)]))

#use string.digits to create a random number of length 5
print("".join([random.choice(string.digits) for _ in range(5)]))
#use string.ascii_letters to create a random word of lenth 5
print("".join([random.choice(string.ascii_letters) for _ in range(5)]))
#combination of number and letters
print("".join([random.choice(string.digits + string.ascii_letters) for _ in range(5)]))
