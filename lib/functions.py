#!/usr/bin/env python3

#greet_programmer
def greet_programmer():
    print("Hello, programmer!")
greet_programmer()

#greet
def greet(name):
    print(f"Hello, {name}!")
greet("James")


#greet_with_default
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default()
greet_with_default("Developer")

#add
def add(num1, num2):
    return num1 + num2
result = add(3,4)
print(result)

#Halve
def halve(number):
    if not isinstance(number, (int, float)):
        return None
    return number / 2
result = halve(8)
print(result)





