
#############################################
#
# Implement the pow operation ( x**y, x^y ) using
# a while block and the variables 'base' and
# 'exponent', so the result is base^exponent.
# Print the result.
#
#############################################

base = 2
exponent = 4

result = base
while exponent > 1:
	result = result * base
	exponent = exponent - 1

print (result)