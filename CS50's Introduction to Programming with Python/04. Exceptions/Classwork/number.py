# Catches a value error

try:
    x = int(input("What's x? "))
    print(f"x is{x}")

except:
    print("x is not an integer")