# Author: Ileana Hernandez
# Date: 02/03/2021
# Description: Recursive function that returns the product of two integers

def multiply(x, y):
    if (x == 0 or y == 0):
        return 0            #any number multiplied by zero is zero
    if (y > 0):
        return (x + multiply(x, y - 1)) #adding numbers one by one, instead of using multiplication

x = 7
y = 4
print(multiply(x, y))     #calling the function
