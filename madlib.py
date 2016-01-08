#mad lib program
def coldNovember():
	adj1 = raw_input("Enter an adjective: ")
	adj2 = raw_input("Enter an adjective: ")
	adj3 = raw_input("Enter a Bird type: ")
	adj4 = raw_input("Room in a house: ")
	verb1 = raw_input("Enter a past tense verb: ")
	verb2 = raw_input("Enter a verb: ")
	name1 = raw_input("Enter a name: ")
	noun1 = raw_input("Enter a noun: ")
	liquid1 = raw_input("Enter a liquid: ")
	verb3 = raw_input("Enter a verb ending with ing: ")
	bodypart1 = raw_input("Enter a part of body: ")
	pluralnoun1 = raw_input("Enter a plural noun: ")
	verb4 = raw_input("Enter a verb ending with ing: ")
	noun2 = raw_input("Enter a noun: ")

	print "It was a " + adj1 + ", cold November day."
	print " I woke up to the " + adj2 + " smell of " + adj3 + " roasting in the " + adj4 + " downstairs."
	print " I " + verb1 + " down the stairs to see if I could help " + verb2 + " the dinner."
	print " My mom said, see if " + name1 + " needs a fresh " + noun1 + "."
	print " So I carried a tray of glasses full of " + liquid1 + " into the " + verb3 + " room."
	print " When I got there, I couldn't believe my " + bodypart1 + "!"
	print " There were " + pluralnoun1 + " " + verb4 + " on the " + noun2 + "! "

def main():
    while True:
        again = raw_input("Would you like to play? Enter yes/no: ")

        if again == "no":
            print ("Thanks for Playing!")
            return
        elif again == "yes":
            print ("Lets play..")
            coldNovember()
        else:
            print ("You should enter either \"yes\" or \"no\".")

if __name__ == "__main__":
    main()
    