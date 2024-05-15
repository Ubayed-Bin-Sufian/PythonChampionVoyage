# use of infinite loop

while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")



"""
# Removing the error using else

try:
    x = int(input("What's x? "))    
except ValueError:
    print("x is not an integer")
else:
    print(f"x is{x}")
"""



"""
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")  # Error occurs earlier
"""