def main():
    # Prompt the user for input
    user_input = input("Type your sentence: ").strip()

    # Call convert on the user input and print the result
    print(convert(user_input))


def convert(emoticons):
    # Convert :) to 🙂 and :( to 🙁
    return emoticons.replace(":)", "🙂").replace(":(", "🙁")


main()
