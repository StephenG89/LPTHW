
types_of_people = 10
# Use types_of_people inside x
x = f"There are {types_of_people} types of people."
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# Printing x will evaluate types_of_people to a string
print(x)
# Printing y will evaluate binary and do_not to strings
print(y)

print("I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
# This leaves an open variable declaration, to be used later.
joke_evaluation = "Isn't that joke so funny?! {}"

# This uses the open variable and populates it with hilarious
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
