# YO

def palindrome(s):
	return s == s[::-1]
if __name__ == '__main__':
	s = raw_input("Enter a string: ")
	if palindrome(s):
		print "yay a palindrome"
	else:
		print "Oh no, not a palindrome"