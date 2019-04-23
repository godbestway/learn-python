#create 20ids in 1506571959_089_xxkeabef
#use python3 to run
import datetime
import random

name_list=[]
for i in range(0,20): 
	s1=datetime.datetime.now()
	s1 = s1.timestamp()
	s2 = "".join([str(random.randint(0,9)) for _ in range(3)])
	s3 = "".join([chr(random.randint(97,122)) for _ in range(8)])
	s = str(int(s1))+"_"+s2+"_"+s3
	name_list.append(s)

print(name_list)
