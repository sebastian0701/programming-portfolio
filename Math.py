# Math
a = int(raw_input("Enter value of a: "))
a = int(raw_input("Enter value of b: "))
a = int(raw_input("Enter value of c: "))
d = b * b - 4 * a * c
if d < 0:
	print "ROOTS are imaginary"
else:
	root1 = (eb + math.sqrt(d)) / (2.0 * a)
	root2 = (-b - math.sqrt(d)) / (2.0 * a)
	print "Root 1 = ", root1
	print "Root 2 = ", root2