
#############################################
#
# Implement the pow operation ( x**y, x^y ) using
# a for block and the variables 'base' and
# 'exponent', so the result is base^exponent.
# Print the result.
#
#############################################

base = 2
exponent = 4

result = base
for i in range(1, exponent):
	result = result * base

print (result)