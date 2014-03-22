#############################################
#
# Sometimes appending is not the way to add new
# elements to a list. For example, if you have two
# lists and you append one to the other, ... well, 
# see what happens.
#
#############################################

the_list = [1, 2, 3, 4, 5]
another_list = [6, 7, 8, 9, 10]

#
# append another_list to the_list
#

the_list.append(another_list)
print (the_list)

#############################################
#
# What we really wanted is to get this:
# 	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# The method we want to use in this case is 
# called extend(). 
#
# Use it just like append() and print the result
#
#############################################

the_list = [1, 2, 3, 4, 5]
another_list = [6, 7, 8, 9, 10]

the_list.extend(another_list)
print (the_list)