# I want to create a function which will take input integer and print the paramid pattern of *

def print_pyramid(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

x = int(input("Enter the number of levels for the pyramid: "))
print_pyramid(x)