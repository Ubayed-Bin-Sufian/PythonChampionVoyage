def main():
    a = int(input("What's a? "))
    if is_even(a):
        print("Even")
    else:
        print("Odd")

#More improved version
def is_even(x):
    return x % 2 == 0

main()

"""
#Improved version of the following function
def is_even(x):
    return True if x % 2 == 0 else False
"""

"""
#Custom function that returns bool
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
"""
