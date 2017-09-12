#Import the variable argv from system module
from sys import argv

#Unpack argv to the two variables
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL+C (^C).")
print("If you do want that, hit RETURN.")

#Pause for user input
input("?")

#Open the file object in write mode (auto-truncates)
print("Opening the file...")
target = open(filename, 'w')

#Delete the contents, this actually isn't necessary as we opened in write mode.
print("Truncating the file. Goodbye!")
#target.truncate()

print("Now I'm going to ask you for three lines.")

#Prompt user for new lines for file
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

#Write the 3 lines on individual lines
target.write(f"{line1}\n{line2}\n{line3}")

print("And finally, we close it.")
target.close()
