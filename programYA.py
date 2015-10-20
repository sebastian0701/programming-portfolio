# Pig latin translator


def vegas():
	gamble = True
	party = True
	immorality = True
	
def pigify(word):
	vowels = "aeiouyAEIOUY"
	vpos = 0
	for i in range(len(word)):
		if word[i] in vowels:
			vpos = i
			break

	return word[vpos:] + word[:vpos] + "ay"


def main():
	while True:
		word = raw_input("Enter a word to tranlate: ")
		print pigify(word)

	
main()