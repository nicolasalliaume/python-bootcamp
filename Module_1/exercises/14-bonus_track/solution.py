
#############################################
#
# Write a function that tells you if the three
# given numbers are in ascending order or not
#
#############################################

def are_ascending(number1, number2, number3):
	return number1 <= number2 and number2 <= number3

	# another [hacker] way to do it:
	# return number1 <= number2 <= number3


print (are_ascending(1, 2, 3))
print (are_ascending(1, 2, 1))
print (are_ascending(5, 2, 1))
print (are_ascending(8, 15, 160))