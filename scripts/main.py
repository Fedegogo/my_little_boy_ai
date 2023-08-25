import openai
import os

# Load the API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

messages = []

# Prompt user for input
message = input("User: ")
print(message)

# Add each new message to the list
messages.append({"role": "user", "content": message})
print(messages)

# Request gpt-3.5-turbo for chat completion
response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

# Print the response and add it to the messages list
chat_message = response['choices'][0]['message']['content']
print(f"Bot: {chat_message}")