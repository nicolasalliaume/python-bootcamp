
#############################################
#
# Write 2 functions from that calculate the sum of 
# 'number1' and 'number2' times 'number3'.
#
# One function must implement the adding part, 
# and the other must implement the multiplying part.
#
# The result must be  returned.
#
#############################################

def add(number1, number2):
	return number1 + number2

def product(number1, number2):
	return number1 * number2


num1 = 5
num2 = 10
num3 = 2
print (product(add(num1, num2), num3))