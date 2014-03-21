#############################################
#
# 'the_multi_list' contains elements of different
# types. Iterate over 'the_multi_list' and print
# the elements, unless the element is a list. In
# that case, print each of the elements of that
# child list.
#
# Tip: The 'type()' fucntion can be helpful
#
#############################################

the_multi_list = [1, 2, [3, 4, 5], 7, 8, [9, 10, 11]]

for item in the_multi_list:
	if type(item) is list:
		for subitem in item:
			print (subitem)
	else:
		print (item)