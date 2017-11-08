#--------WHILE LOOP FUNCTION-----------------
def LoopFcn(Lim, inc):
    i = 0
    numbers = []

    while i < Lim:
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + inc
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    return numbers
#-------------------------------------------

numbers = LoopFcn(6, 2)

print("The numbers: ")

for num in numbers:
    print(num)
