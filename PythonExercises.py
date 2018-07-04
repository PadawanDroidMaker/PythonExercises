# Excercises from https://www.practicepython.org/
# ***********************************************

# Exercise 1: Character input
# ***************************
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that
# they will turn 100 years old.

# Extras:
# ********

# 1- Add on to the previous program by asking the user for another number 
#    and printing out that many copies of the previous message.
#    Print out that many copies of the previous message on separate lines.

# Solution:
# **********

#name = input("Please enter youn name: ")
#age = int (input("Please enter your age: "))
#restTo100= 100 - age
#yearToReach100 = 2018 + restTo100
#iterations = int (input("Please enter number of times: "))
#print ("\n")
#n = 0
#while (n < iterations):
#    print (name + ", you will be 100 years old in: " + str(yearToReach100))
#    print ("\n")
#    n+=1

# ***************************************************************************
# Exercise 2: Odd or Even?
# ************************
# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.

# Extras:
# *******
# 1- If the number is a multiple of 4, print out a different message.
# 2- Ask the user for two numbers: one number to check (call it num)
#    and one number to divide by (check).
#    If check divides evenly into num, tell that to the user.
#    If not, print a different appropriate message.

# Solution:
# *********

#number = float (input("Please enter a number: "))
#print ('\n')
#if (number % 2 == 0):
#    # extra 1:
#    if (number % 4 == 0):
#        print ("The number you entered is even and divisible by 4")
#    else:
#        print("The number you entered is even")

# Exercise 2 cont: extra 2
# ************************
        
#num = float (input("Please enter a number to check: "))
#check = float (input("Please enter a number to check against: "))
#print ('\n')
#quotient = num % check
#if (quotient == 0):
#    print (str(num) + " is divisible by " + str(check))
#else:
#    print (str(num) + " is NOT divisible by " + str(check))

# ****************************************************************************
# Exercise 3: List less than 10
# *****************************
# Take a list, say for example this one:

#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 10.
#
# Extras:
# *******
# 1- Instead of printing the elements one by one, make a new list that has all the elements
#    less than 5 from this list in it and print out this new list.
#    Write this in one line of Python.
# 2- Ask the user for a number and return a list that contains only elements from the original
#    list a that are smaller than that number given by the user.

# Solution:
# *********

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#for i in a:
#    if (a[i] < 10):
#        print (a[i])
#        print ('\n')
        



































   