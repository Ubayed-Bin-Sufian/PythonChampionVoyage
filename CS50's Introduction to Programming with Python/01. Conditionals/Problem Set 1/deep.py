# Ask for input
question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# output "Yes" if the user inputs 42 or (case-insensitively) forty-two or forty two
if question.strip() == "42":
    print("Yes")

elif question.lower().strip() == "forty two":
    print("Yes")

elif question.lower().strip() == "forty-two":
    print("Yes")

# Otherwise output "No"
else:
    print("No")
