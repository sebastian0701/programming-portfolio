# Python Learning Exercises

# Functions
def echo(thing):
	return thing
	
def swap(s,c):
	return c,s


def main_function():
	print "testing echo('marco'): ", echo('marco')
	print "testing echo('shut up '): ", echo('no, you shut up')
	print "testing echo('fame', 'fortune')", swap('fame', 'fortune')


#Arithmetic Function
def reverse(x):
	return -x

def plus(s,c):
	return s + c

def diff(x, y):
	return x - y

def abs_diff(d, b):
	return d 



def main_arithmetic():
	print "test reverse(3): ", reverse(3)
	print "test reverse(-3): ", reverse(-3)
	print "test plus(150,-50): ", plus(150,-50)
	print "test diff(12, 5): ", diff(12,5)


def main():
	main_function()
	main_arithmetic()
	
main()