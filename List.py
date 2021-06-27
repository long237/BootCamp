#Python List

#Variables like x, y, z can only store one value at a time.
#What do you do if you need to store many values at once?

# 1)Accessing a list
#Creating a list
mylist = ["Go", "Beach", "hello", "world"]

print(mylist)

#Similar to String you can access values inside a list using indexes (position numbers)
print(mylist[1])

#Accessing the last element using negative numbers works too
print(mylist[-1])

#What happened if you try to access a value that doesnt exist on the list?
#print(mylist[99])

#You will get "Index out of range error". One of the most common error when coding :)


#Accessing many values at once
sport = ["soccer", "basketball", "baseball", "football", "hockey", "tennis"]

#Access items 1 to 3. Value at index 4 is not included
print(sport[1:4])

# Accessing till the end of a list
print(sport[2:])

#Accessing from the beginning of a list
print(sport[:3])

#You can store different data types in a list. All values in a list does not have to be the
#same data type

mixlist = ["Go", "Beach", True, 22, 3.14, "hello", "world",]

print(mixlist)



# 2)Modifying values of a list

ranlist = ["Go", "Beach", "hello", "world"]

ranlist[2] = "hi"

#Check the values inside the list after modification
print(ranlist)

#You can also change many items in a list at once
ranlist[1:3] = ["shark", "whale"]
print(ranlist)



#   3) Adding items to a list
a = ["baseball", "basketball", "soccer", "tennis"]

#Using the method append() to add a new value to the back of the list
a.append("hockey")
print(a)

#What if you want to insert a new value into a specific position instead? Use insert()
a.insert(1, "football")
print(a)


#   4)Removing values from a list
crypto = ["bitcoin", "dogecoin", "etherium"]

#You can specify the index of what element to remove. If it is blank the last value will be deleted
crypto.pop(1)
print(crypto)

#Removing a value using remove() function
crypto.remove("bitcoin")
print(crypto)
