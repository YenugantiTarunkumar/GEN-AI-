name = input("What is your name? ")

print("Hello", name + "!")
print("You can talk to me. Type 'bye' or 'exit' to stop.")

while True:
    message = input("You: ").lower().strip()

    if "bye" in message or "exit" in message:
        print("Bot: Goodbye", name + "!")
        break

    elif "hello" in message or "hi" in message:
        print("Bot: Hello", name + "! How are you?")

    elif "how are you" in message:
        print("Bot: I am doing great! Thanks for asking.")

    elif "your name" in message:
        print("Bot: My name is Python Bot.")

    elif "what can you do" in message:
        print("Bot: I can answer simple questions and have a conversation.")

    else:
        print("Bot: Sorry, I don't understand that.")