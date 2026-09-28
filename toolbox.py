# Function 1 - double: Multiplies a number by 2
def double(number):
    return number * 2


# Function 2 - is_pass: Returns True if score >= 50, otherwise False
def is_pass(score):
    return score >= 50


# Function 3 - greet: Formats a greeting with a default value of "Hello"
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


# Testing the functions
print(double(7))
print(double(10))
print(is_pass(80))
print(is_pass(20))
print(greet("Amina"))
print(greet("Brian", "Habari"))
