#Introduction to Python

#Comments
#Any line with the symbol "#", at the begining will be ignored by Python
#Such as this one

#Print Statements
print("Hello World")
print('Hello World')

#Numbers and variables
#Just like in math, you can save values such as number into variables

#Data types that you should know and will be using a lot:
    # 1. Interger
    # 2. Float
    # 3. String
    # 4. Bool (Boolean)
x = 5       #integer
y = 2.64    #float
z = 3.14

u = True    #bool
v = False   #bool

r = "5"     #String
s = "3.14"  #String


#Printing numbers to the console

print("Value of x:", x)

#What would be printed if we try to print "u" and "v"

print("Value of u: ", u)
print("Value of v: ", v)

#Reassigning variables and how it works.
x = 99
print("Value of x:", x)

#Saving Strings to a variable

a = "Hello"
b = "Long"

#Combingning and printing Strings (String Concatenation)
#What would be the value of c ?

c = a + b
print(c)
print("Hello" + b)
print("hello" + "Long")

#Python Operators
#Python contains your normal math operators which are straight forward
#and does what you expect them too

m = 5
n = 2
r = "5"
s = "2"

#Operators that are mostly used for math
#Addition

p = m + n
print("Value of p:", p)

#What happened when we add 2 strings?
p = r + s
print("Value of p:", p)

#How would we solve this problem??
#You can change the data type from one to another using "Casting"

#Subtraction
p = m - n
print("Value of p:", p)

#Multiplication
p = m * n
print("Value of p:", p)

#Division
p = m / n
print("Value of p:", p)

#Exponential
p = m ** n
print("Value of p:", p)

#Comparison operators
#Aside from operators that are used for math and string concatenations,
#there are also operators for comparing value between variables

j = 3
k = 8

#Comparison operators will return a boolean value in order words either True or False
#These values can be saved for later used or simply discarded

#Equal comparisons and not equal
L = (j == k)
print("Value of L:", L)

L = (j != k)
print("Value of L:", L)


#Since the operator "=" or equal sign is used to assign a value to a variable
#The operator "==" is used to compare to see if the two values to see if they are equal or not

#Less than and Less than or equal to

L = (j < k)
L = (j <= k)

#More than and more than or equal to

L = (j > k)
L = (j >= k)

#Logial operators such as And, Or, Not
#There are words in Python that are reserved for functions and operators such as these
#What if you want to do more than one comparison on one single line?

x = 4

shark = x < 10 and x > 2
print("Value of shark: ", shark)

shark = x < 10 or x > 2

shark = not(x < 10)


#Python If...else statements (also know as Conditional statement)
#What if you want a certain things to happen when a condition is met??

#Print "Go Beach" if i > 5

i = 100
if i > 5:
    print("Go Beach")

#You can also do more in the "if block" such as adding another print line 

#3 keyword to remembers for conditional statement
    # 1. If
    # 2. Else if (elif)
    # 3. Else

#This block will execute from a top down order one line after another
#Which statement to be printed will depends on the value of "i"
#Indentation in Python is very important since it signified what statement will be executed
#depends on which condition is met. You will get an error
    
i = 99
if i > 200:
    print ("Hello World")
elif i > 10:
    print ("Go Beach")
else:
    print ("GME to the moon")

#For loops.
#Let say you want to print "Hello World" 5 times, how would you do it without writing 5 "print" statement?
#Also becareful with the value of "i" when you work with with loops and the range() function

for i in range(5):
        #print("Value of i:", i)
        print("Hello World")

#The same can be achieve using a while loop:

i = 0
while i < 5:
    print("Go Beach")
    i = i + 1 

#Functions for user input:
#The function will return a String when the user enter a value which means if you are asking for a number
#and you want to do math with it, you will have to cast it to an interger or a float

name = input("Enter your name: ")
print ("Hello, " + name)
    











