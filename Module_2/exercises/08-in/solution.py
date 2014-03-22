#############################################
#
# A good way to test if an element is inside a
# list is using 'in'. For example:
#
#		'some' in ['there', 'are', 'some', 'elements']
#
#	will return True
#
# Use it to print if the given elements 'elems'
# are inside 'the_list'
#
#############################################

the_list = ['some', 'nonsense', 'elements', 'of', 'a', 'list', 'are', 'written', 'in', 'here']

elems = ['a', 'see', 'Universe', 'some', 'house', 'jaguar', 'list']

for elem in elems:
	if elem in the_list:
		print (elem, 'is in the list!')
	else:
		print (elem, 'is not in the list!')