import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if re.search(r"\b(hi|hello|hey|hola)\b", user_input):
        return "Hello! How can I assist you today?"

    # Asking about chatbot
    elif re.search(r"\b(who are you|what can you do)\b", user_input):
        return "I'm a simple chatbot here to answer your questions!"

    # Time-related queries
    elif re.search(r"\b(time|clock|what time is it)\b", user_input):
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%I:%M %p')}."

    # Help-related
    elif re.search(r"\b(help|support|assist)\b", user_input):
        return "Sure, I'm here to help! Tell me what you need assistance with."

    # Goodbye
    elif re.search(r"\b(bye|goodbye|see you|exit|quit)\b", user_input):
        return "Goodbye! Have a great day!"

    # Fallback/default response
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Driver loop
print("Chatbot: Hi! I'm your virtual assistant. Type 'exit' to end the chat.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Chatbot: Goodbye! Take care.")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
