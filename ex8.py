
# Define a variable called formatter with 4 arguments
formatter = "{} {} {} {}"

# Use the format function to pass the arguments and print
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Four Score",
    "And seven years ago",
    "Something happened",
    "I forget what it was"
))
