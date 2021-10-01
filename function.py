#Python function

#When writing code you often find many lines of code bundle up into a mess.
#Function is there to help you group code together which improve readability as well as
#as reusibility.

#I) Defining functions:

#Till now you probably are familiar with some function such as print()
#print() is a built-in function that is in Python library that allow you to print a String to a console

#print("Go Beach")

#However, you can make you own functions depends on the purpose of your program.
#You can define a new function using the keyword "def" follows by the function name and a set of parentheses

def say_hello():
    print("Hello World! My name is John")
print("Go beach")

#Run the file and see if anything happens on the console. 

#Codes within the function don't run untill you call the function

say_hello()
say_hello()
say_hello()

#II)Arguments:

#Functions might or might not have arguments. Arguments are information that can be passed into a function to be used

#For example, a function that takes in a random user's name and say hello to that person

def hello(user_name, major):
    print("Hello", user_name, "from CSULB major in ", major)

hello("Elizabeth", "Business")

#A function can also do some calculation and return a value to be saved
#into a variable for later use.
#If you don't save the value that is returned by the function. It will just disappear. 
#Example 2: a function that ask for 2 numbers and provide the sum.
def sum(a, b):
    total = a + b
    y = 20
    return total
    print("Hello world")

num1 = 2
num2 = 3
c = sum(num1, num2)
c = 2 * c
print("The sum of a and b is: ", c)

#III) Scope:
#Some variables are only accessible within the place that they are created

a = 50
def rand_function():
    x = 22
    print("Value of x within the function:", x)
    print(x)
    # return x

rand_function()
# x = 100
# print(x)            #What value would this line print??
# x = rand_function()
# print("Val of x: " , x)

#If you call function rand_function() then what value would print?
#Although both variables are name "x", they are not the same variable.
#In other words, they are 2 different variables with the same name.

#How would this benefits us?
#It lets you reuse variable name without messing up your own code or someone elses code.
#If someone else is using the variable for something else and you reassign it with a different value
#that means that their code won't be working as expected anymore. 



#III)Main function:

#Most programs have a main() function which is just a function that is called "main".
#When you call the main() function the entire code get executes.


#Example of a simple program that ask for the user's name and say hello to that user

def get_name():
    name = input("Enter your name here:")
    return name

def get_major():
    return input("What is your major:")

def main():
    name = get_name()
    hello(name)
    major = get_major()
    print(name, "major is", major)
    

# main()


rand_function()