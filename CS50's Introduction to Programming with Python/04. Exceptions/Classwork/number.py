# Catches a value error

try:
    x = int(input("What's x? "))
    
except:
    print("x is not an integer")

print(f"x is{x}")