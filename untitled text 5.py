# Sales Man Salary
basic_salary = 1500
bonus_rate = 200
commision_rate = 0.02
numberofcamera = int(raw_input(("Enter the number of the inputs sold: "))
price = float(raw_input("Enter the total prices: "))
bonus = (bonus_rate * numberofcamera)
commision = (commision_rate * numberofcamera * price)
print "Bonus	    = %6.2f" % bonus
print "commision	= %6.2f" % commision
print "gross salary = %6.2f" % (basic_salary + bonus + commision)
