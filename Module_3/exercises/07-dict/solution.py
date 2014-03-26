#############################################
#
# A dictionary can be created using the method
# 'dict()', which gives us flexibility to construct
# a dictionary from another structure, for example,
# a list.
# 
# Use dict() to create a dictionary from the
# given list and print it.
#
#############################################

the_list = [('name', 'Robert'), ('age', 28), ('country', 'Canada'), ('children', ['Sam', 'Susan'])]

print (dict(the_list))  

# Notice the first element of each tuple is the key 
# of the dictionary and the second element is the value