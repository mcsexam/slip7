responses = {
    "hi": "Hello there! How can I help you today?",
    "hello": "Hi! How can I assist you?",
    "hey": "Hey! What can I do for you?",
    "how are you": "I'm just a computer program, but I'm here to help you.",
    "bye": "Goodbye! Have a great day.",
    "exit": "Goodbye! If you have more questions, feel free to come back."
}

def chatbot(user_input):
    user_input = user_input.lower()
    response = responses.get(user_input, "I'm not sure how to respond to that. Please choose from the predefined inputs: 'hi', 'hello', 'hey', 'how are you', 'bye', 'exit'")
    return response

print("Simple Chatbot: Type 'bye' or 'exit' to end.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye" or user_input.lower() == "exit":
        print("Simple Chatbot: Goodbye!")
        break
    response = chatbot(user_input)
    print("Simple Chatbot:", response)
