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


#Boolean


def reverse(zack):
	return not zack
	
def band(a, b):
	if a==True and b==True:
		return True
	else:
		return False	
	
def bor2(a, b):
	return a or b
	
	
def main_boolean():
  print "test reverse(True): ", reverse(True)
  print "test reverse(False): ", reverse(False)
  print "test reverse(1): ", reverse(1)
  print "test reverse(0): ", reverse(0)
  print "test band(True, True): ", band(True, True)
  print "test ban2(True, False): ", band2(True, False)








def main():
	main_function()
	main_arithmetic()
	main_boolean()
	
main()