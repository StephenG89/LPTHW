
name = 'Stephen Gallagher'
age = 28
height = 163 #cm
weight = 68.5 #kg
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} cm tall.")
print(f"He's {weight} pounds heavy.")
print("Actually he's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth}, depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

height_in = height * 0.393701 # in = cm * 0.393701
weight_lbs = weight * 2.20462

print(f"His height in inches is {height_in}")
print(f"His weight in lbs is {weight_lbs}")
