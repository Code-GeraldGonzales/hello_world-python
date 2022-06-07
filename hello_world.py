# 1. TASK: print "Hello World"
print( "Hello World" )
# 2. print "Hello Noelle!" with the name in a variable
name = "Jerry"
print( "Hello" "," " " "Jerry")	# with a comma
print( "Hello" " "+ name)	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 23
print( "Hello", "23")	# with a )	# with a comma
print( "Hello" " "+ str(23))	# with a )	# with a +	-- this one should give us an error!
# 4. print "I love to eat tacos and mango." with the foods in variables
fave_food1 = "tacos"
fave_food2 = "mango"
print( "I love to eat {} and {}.".format("tacos", "mango") )
# with .format()
print( f"I love to eat {fave_food1} and {fave_food2}." )
# with an f string
