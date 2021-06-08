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













