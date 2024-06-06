# Practice from https://www.youtube.com/watch?v=q5HiD5PNuck

# Import the OpenAI library
import openai

# Set the API key for OpenAI
openai.api_key ="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"

# Define a function to interact with GPT
def chat_with_gpt(prompt):

    # Call the OpenAI API with the provided prompt
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    # Return the generated response after stripping whitespace
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:

        # Start an infinite loop to chat with the user
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        # Get response from the chat_with_gpt function
        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
