#############################################
#
# Please help me solve this big mess!!
# Following there's a list containing elements
# of different types.
#
# Print all the elements following these rules:
#	- If it is a number or string, just print it
#	- If it is a list, print each of the elements
#	- If it es a tuple, print each of the elements
# 	- If it is a dictionary, print each of the values
#
# Tip: remember type() function? It will tell you
#  	the type of a given variable (list, dict, tuple, ...)
#
#############################################

big_mess = ['Even', ('if', 'you'), ['fall', 'on', 'your'], {1: 'face', 2: "you're", 'other': 'still'}, 'moving', ['forward', '.']]

for item in big_mess:
	if type(item) is list or type(item) is tuple:
		for subitem in item:
			print (subitem)
	elif type(item) is dict:
		for subitem in item.values():
			print (subitem)
	else:
		print (item)