
s = "dABjs_123r45"
x = []
for i in s:
	if i.isalpha():
		if i.islower():
			x.append(1)
		if i.isupper():
			x.append(2)
for i in s:
	if i.isdigit():
		x.append(3)
for i in s:
	if i == "_":
		x.append(4)
y = set(x)
##print y
z = set([1,2,3,4])
if y&z == z:
	print "good"
