#############################################
#
# A file can be read as a whole (using read() 
# as in our last exercise) or line by line using
# readline()
#	
# Use readline() to read the given file and print
# each of the lines adding the line number at the
# beginning.
#
# https://docs.python.org/3.3/tutorial/inputoutput.html#reading-and-writing-files
#
# Tip: checkout what strip() does to a string.
#
#############################################

the_file = 'the_file.txt'

f = open(the_file, 'r')
line_count = 0

l = f.readline()
while l:
	line_count += 1
	print (line_count, l.strip()) # checkout what strip() does to a string!
	l = f.readline()

f.close() # don't forget to close the file!