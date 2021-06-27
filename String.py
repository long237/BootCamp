#Python String

#String is one of the variable type that you will be using a lot.
#You can do a lot of things with strings

#1) Accessing each letter in a string

a = "hello world"

#Guess what this line will print. 
print( a[1])

#You can access any characters in the String by using the name of the variable and
#and giving it an index (the position of the letter).
#Counting forward index will start at 0. Spaces also count.

#Instead of going forward you can also use negative numbers to access letters from the back
print(a[-1])

#2) Slicing String

b = "Go Beach"

#You can access many characters in a String at once
#Keep in mind that the letter at position 3 is included while 6 is not.  
print(b[3:6])

#Slicing from the start of the String
print(b[:6])

#Vice versa for slicing to the end
print(b[1:])


#3) Contatenate String (Putting different strings together into one)

x = "hello"
y = " world"

z = x + y

print(z)

#4) Escape characters:

#Since the operator "" is used to create strings, how would we use it if you want to include it in the String?

c =  "\"GME\" to the moon"
print(c)

#Or if you want to go down to a new line.
print("Go Beach \nHello world")

