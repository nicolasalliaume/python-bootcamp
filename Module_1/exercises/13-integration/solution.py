
#############################################
#
# Write a program that prints a greeting to the
# given person, adding as many '!' simbols at the
# end as wanted.
#
#############################################

def greet(greeting, name, number_of_exclamations):
	exclamations = ""
	for i in range(number_of_exclamations):
		exclamations = exclamations + "!"
	print (greeting, name + exclamations)


# Test the program
greet("Nice to meet you,", "Nicholas", 2)
greet("Long time no see,", "Richard", 5)
greet("How nice to see you,", "Rachel", 1)
greet("Give me five,", "Nicholas", 10)