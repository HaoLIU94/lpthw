#!/usr/bin/python

import Tkinter
top = Tkinter.Tk()
# Code to add widgets will go here...
top.mainloop()

print "Hello World!"
#good this is how we write comments
print("Hao",25+30/6)
print(3+2<5-7)

print(5>-2)
print(3+2+1-5+4%2-1/4+6)

cars=100
space_in_a_car = 4.0

string = 'Nihao'

print(space_in_a_car)
print(string)
print("let me say "+string)
round(1.733333)

#raw_input("\n\nPress the enter key to exit.")

import sys; x = 'foo'; sys.stdout.write(x + '\n')

counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print counter
print miles
print name

a,b,c = 1,2,"john"
print a,b,c

str = 'Hello World!'

print str          # Prints complete string
print str[0]       # Prints first character of the string
print str[2:5]     # Prints characters starting from 3rd to 5th
print str[2:]      # Prints string starting from 3rd character
print str * 2      # Prints string two times
print str + "TEST" # Prints concatenated string

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list          # Prints complete list
print list[0]       # Prints first element of the list
print list[1:3]     # Prints elements starting from 2nd till 3rd 
print list[2:]      # Prints elements starting from 3rd element
print tinylist * 2  # Prints list two times
print list + tinylist # Prints concatenated lists

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
#tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list

a = 1
b = 20
list = [1, 2, 3, 4, 5 ];

if ( a in list ):
   print "Line 1 - a is available in the given list"
else:
   print "Line 1 - a is not available in the given list"

count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1

print "Good bye!"
'''
var = 1
while var == 1 :  # This constructs an infinite loop
   num = raw_input("Enter a number  :")
   print "You entered: ", num

print "Good bye!"
'''
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"
'''
flag = 1

while (flag): print 'Given flag is really true!'

print "Good bye!"
'''
for letter in 'Python':     # First Example
   print 'Current Letter :', letter

fruits = ['banana', 'apple',  'mango']
for liuhao in fruits:        # Second Example
   print 'Current fruit :', liuhao

print "Good bye!"

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print 'Current fruit :', fruits[index]

print "Good bye!"

for num in range(10,20):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the second factor
         print '%d equals %d * %d' % (num,i,j)
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print num, 'is a prime number'

var1 = 'Hello World!'
var2 = "Python Programming"

print "var1[0]: ", var1[0:5]+'NIhao'
print "var2[1:5]: ", var2[5:]

print "My name is %s and weight is %d kg!" % ('Zara', 21)

para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print para_str

str = "this is string example....wow!!!";

print "str.capitalize() : ", str.capitalize()

import time;  # This is required to include time module.

ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks

import calendar

cal = calendar.month(2008, 1)
print "Here is the calendar:"
print cal

def printme( str ):
   "This prints a passed string into this function"
   print str
   return;

# Now you can call printme function
printme("nihao")

def printinfo( name, age ):
   "This prints a passed info into this function"
   print "Name: ", name
   print "Age ", age
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )

def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print "Output is: "
   print arg1
   for var in vartuple:
      print var
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )

import math
content = dir(math)

print content

print math.pi


str = input("Enter your input: ");
print "Received input is : ", str


try:
   fo = open("foo.dat", "r+")
   fo.write("This is my test file for exception handling!!")
except IOError:
   print "Error: can\'t find file or read data"
else:
   print "Written content in the file successfully"
   fo.close()

fo = open("foo.dat", "r+")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace


close =int(raw_input());
if close==1:
   print "Close file",fo.name
   print fo.read(10)
   print fo.tell()
   fo.close()
else:
   print "keep",close ,"open"

