# Secret Decoder

# Save a message 


def main ():
	file_name = raw_input("Enter a file name")
	old_message = open(file_name)
	print "your old message said: "
	print old_message.read()
	
	message = raw_input("Enter a message: ")
	plain_message = open(file_name, "w")
	plain_message.write(message)
	plain_message.close()
	
	
	
	
main()