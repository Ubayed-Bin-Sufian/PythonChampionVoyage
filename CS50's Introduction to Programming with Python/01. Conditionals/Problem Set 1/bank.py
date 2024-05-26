def main():

#prompts the user for a greeting. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
    greeting =input("Greeting: ").strip().lower()

#If the greeting starts with “hello” but also “hello there”, “hello, Newman” etc. output $0
    if greeting.startswith("hello"):
        print("$0")

#If the greeting starts with an “h” (but not “hello”), output $20
    elif greeting.startswith("h"):
        print("$20")

#Otherwise, output $100
    else:
        print("$100")

main()
