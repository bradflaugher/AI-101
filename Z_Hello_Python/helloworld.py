#simple print statement
print "Hello, World."

#variable assignment, and another print statement
some_integer = 78
print some_integer + 2

#a loop
for letter in "Helllooo, world":
  if letter != ',':
    print letter

#a loop and an array
for fruit in ["melon","banana","pear"]:
  print "would you you like to eat a %s? We have lots of %ss!" % (fruit,fruit)

#an example of recursion
def remove_maggots(number_to_remove):
  if number_to_remove == 0:
    print "Done"
    return
  elif number_to_remove > 0:
    print "Removing a maggot..."
    number_to_remove = number_to_remove - 1
    remove_maggots(number_to_remove)

#run the function we just made
remove_maggots(100)
