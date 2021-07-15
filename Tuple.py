#Python Tuple

#Similar to a list, a tuple is also used to store any type of the data that you want.
#Attribute of a tuple:
    # +Ordered (Accessible using index)
    # +Unchangeable (Once you made it, cannot add or remove items from within)
    # +Allow duplicates values
    # +All values in a tuple does not have to be the same data type


# oOo 1)Accessing Items oOo:

#Creating a tuple of different fishes (packing a tuple)
mytuple = ("shark", "stingray", "whale", "salmon")

#Getting the first item in the tuple
print(mytuple[0])

#Similarly for other items:
print("This is a very big mamal:", mytuple[2])

#Accessing many items at once
print("These are all salt water fish:", mytuple[0:3])
print()


# oOo 2)Unpacking a tuple: oOo

(a, b, c, d) = mytuple

print("Our school mascot: ")
print(a)
print()


print("Has a very similar look to a kite: ")
print(b)
print()

print("One of the largest mamal on the planet: ")
print(c)
print()

print("Swim up-stream to reproduce:")
print(d)
print()


# oOo 3)Using loops to access items in a tuple oOo

#Similar to a list, you can use loops to access all elements in a tuple

#For loop:
for fish in mytuple:
    print(fish)

print()


#Or for loop using index:
for i in range(len(mytuple)):
    print(mytuple[i])
print()

#What would be the difference between the 2 way of using the for loops?
    # +The first one access the item directly therefore you will not know the index of that item
    # +Accessing the item using an index allow you to know where it is located in a tuple

#Using a while loop to access the items:

j = 0
while (j < len(mytuple)):
    print(mytuple[j])
    j = j + 1


    
