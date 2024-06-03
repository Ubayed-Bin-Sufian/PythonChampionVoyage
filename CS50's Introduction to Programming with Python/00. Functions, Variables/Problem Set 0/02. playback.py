#prompts the user for input
sentence = input("Please enter your sentence: ").strip()

#outputs that same input, replacing each space with ...
sentence = sentence.replace(" ", "...")
print(sentence)
