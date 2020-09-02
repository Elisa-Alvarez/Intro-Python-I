# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def evenNum (even):
    if even % 2 == 0:
        return True
    else:
        return False
print(evenNum(4))
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def whatNum (num):
    if num % 2 == 0:
        return "Even!"
    else: 
        return "Odd"
print(whatNum(25))