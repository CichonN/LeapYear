#-----------------------------------------------------------------------
# Neina Cichon
# Assignment Name: Leap Year
# Date: June 13, 2020
#-----------------------------------------------------------------------

# ask user for input and assign to variable
intYear = int(input("Please enter a year: "))

# Make sure year entered are between 1500 and 2200
if intYear > 1500 and intYear <2200:
	if intYear % 4 ==0: # Check if Year is evenly divisible by 4
		if intYear % 100 ==0: # Check if Year is evenly divisible by 100
			if intYear % 400 == 0: # Check if Year is evenly divisible by 400
				# print results
				print("YES!", intYear, " is a leap year!")
			else: 
				print("No, ", intYear, " is not a leap year.")
		else:
			print("YES!", intYear, " is a leap year!")
	else:
		print("No, ", intYear, " is not a leap year.")
else:
	print("Invalid Year.") #return error message because year was not between 1500 and 2200

