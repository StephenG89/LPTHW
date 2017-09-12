#Import the variable argv from the sys module
from sys import argv

#Unpack argv to two variable, script and filename
script, filename = argv

#Open the file and assign object to txt
txt = open(filename)

#Print the contents of the file
print(f"Here's your file {filename}:")
print(txt.read())

#Ask the user to input the filename again
print("Type the filename again:")
file_again = input("> ")

#Reopen the file to txt_again variable
txt_again = open(file_again)

#Print the contents of the file again
print(txt_again.read())

txt.close()
txt_again.close()
