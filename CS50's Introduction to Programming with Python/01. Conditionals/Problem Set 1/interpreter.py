def main():

    #prompts the user for an arithmetic expression
    interpreter = input("Expression: ").strip()

    #convert this into variables
    x, y, z = interpreter.split(" ")

    #Convert the variables to float data type
    x = float(x)
    z = float(z)

    #Call the expression function with the input expression and variables
    expression(interpreter, x, y, z)


def expression(interpreter, x, y, z):

    #calculates and outputs the result as a floating-point value formatted to one decimal place.
    if y == "+":
        ans = x + z

    elif y == "-":
        ans = x - z

    elif y == "*":
        ans = x * z

    #Assume that, if y is /, then z will not be 0.
    elif y == "/":
        if z == 0:
            print("Error: Not divisible by zero")
            return  # Exit the function if z is 0 to avoid division by zero
        ans = x / z

    else:
        print("Error: Missing expression")
        return # Exit the function if an invalid operator is provided

    print(f"{ans:.1f}")

main()
