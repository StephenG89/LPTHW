print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehen passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

# define a function that will calculate and return 3 variables from 1 input.
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 1000
beans, jars, crates = secret_formula(start_point)

# remember this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# Start point becomes 100
start_point = start_point / 10

print("We can also do that this way:")
# formula here will be an array with 3 elements
formula = secret_formula(start_point)
# as formula is an array, * is required in the formatter
print("We'd have {} beans, {} jars and {} crates.".format(*formula))
