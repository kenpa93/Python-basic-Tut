# string methods
a ="sparsh!"
# this print line prints length of the string
print(len(a))
# now this print line will convert all letters of the strings into upper case
print(a.upper())
# this print line now converts all letters of the string into lower case
print(a.lower())
# this print line will remove the the specifid letter from the string
print(a.rstrip("!"))
# this method will replace the the desired letter or string
print(a.replace("sparsh","Srijan"))
# this method will split the string into more items and make them items for list
print(a.split("r"))
# this print line will now turn first letter into a capital letter
print(a.capitalize())
# this print line will now center the output with the given spaces
print(a.center(50))
print(len(a.center(50)))
# this print line will check if the asked letter is at the end of the string
print(a.endswith("!"))
# this print line will show how to find a specific letter or word in the string and print its index number
print(a.find("a"))
# now this printline will tell you the index number of the letter find first occurence of the asked letter
print(a.index("s"))
# this function in print line a-z,A-Z,0-9 if only these is in the string it prints true or else their is any 
# other character it prints false 
print(a.isalnum())
# this print line now will only print true when strings contains from A-Z or a-z or else it will print false
print(a.isalpha())
# in this line we check if all the letters contains all lower case 
# letter then it prints true if any upper case letter 
# appears it will print false
print(a.islower())
# in this line we check if string does'nt contains any escape sequence if it does it prints false or if
# the string does'nt contain any escape sequence then it prints true
print(a.isprintable())
# in this print line we check if their is a space in the string then it prints if space exist
# if string doesn't contain any space in it then it prints flase
print(a.isspace())
# in this print line we check if each word of the sstrings starts with capital letter if it is prints true in output
# if it does not the it returns false
print(a.istitle())
# in this print line we check if all the characters of the string is in capital if it does the prints true in output
# if doesn't the prints false
print(a.isupper())
# in this printline we check if a strings starts with the asked then it prints true in output if starst with
# if it does'nt the pritns false
print(a.startswith("s"))
# in this print line we swap the classes of the letters of the string convert upper case letters to lower case
# if they are in lower case then in upper case
print(a.swapcase())
# in this print line we convert every words first letter in upper class form the string
print(a.title())
