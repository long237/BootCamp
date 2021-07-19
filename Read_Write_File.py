#Reading and Writing to a text file Python

#There are certain times where you are provided with a file that contain information that will be used
#as inputs for your program.

#For instance, imagine writing a program for a car dealership to sell cars online. You then need to
#input the price for different cars base on their type and make. Imagine having to manually input in
#each's cars price. Using the input() function this would take a very long time and it is very tedious.
#On the other hands, you might wanna save the result of your calculation or some random data to a text file
#so that it can later be used.


# oOo 1) Reading from a text file: oOo:

#The open method takes 2 argument. The first argument is the file name and the second argument is the access level for the file

#Some access level:
# 1)Read only ('r')
# 2)Read and Write ('r+')
# 3)Write only ('w')
# 4)Write and read ('w+')
# 5)Append only ('a')
# 6)Append and read ('a+')


myfile = open("randomNames.txt", "r")

#Using readline() to read one line from the file:
print(myfile.readline())

#Reading the entire file line by line:
for name in myfile:
    print(name)

#Reading from a file just give you a string so you can do anything with it
#print("Hello", myfile.readline())

#Closing the file:
#It is a good practice to close the file to prevent unexpected things to happen when you code. 
myfile.close()




# oOo 2)Writing information to a file: oOo:

#When writing to the file using the open function, you should becareful when determining if you should use append or write
#   1)Append: add information to the end of the file
#   2)Write: Overwrite any information that already exist in the file with the new information

file = open("userFile.txt", "a")

#Writing to a file:
file.write("Go Beach \n")

#Adding more lines to the file:
file.write("Shark is CSULB brand new mascot \n")

#Closing the file after modifying the file
file.close()





