#############################################
#
# Use the 'items()' method of a dictionary in
# combination with tuple unpacking to print
# all the elements of the given dictionary
#
# Tip: items() method will return a tuple containing
# 	2 elements: the key and the value
#
#############################################

a_dictionary = {'name': 'Michael', 'age': 34, 'gender': 'Male', 'spouse': {'name': 'Romina', 'age': 32}}

for key, value in a_dictionary.items():
	print ('Key:', key, '- Value:', value)