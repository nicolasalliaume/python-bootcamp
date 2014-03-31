#############################################
#
# Python offers a quite helpful method called 'help()',
# which will show you the available documentation
# of a given method.
#
# A function has been provided to you, containing some
# documentation about it's usage. Print the
# documentation of that method using the help
# function.
#
#############################################

def complex_function(*args):
	'''
		Given any number of numbers (both integers and floating
		point) this method will return a new tuple containing
		the value of each even number given multiplied by 2.
	'''
	return tuple(map(lambda item: item*2, filter(lambda i: i%2==0, args)))


help(complex_function) # notice 'complex_function' does NOT have brackets '()'