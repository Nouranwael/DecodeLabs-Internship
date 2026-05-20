# ============================================================
# Rule-Based AI Chatbot — Week 1 Internship Project
# ============================================================
# This chatbot uses predefined rules (dictionary-based logic)
# to match user input to appropriate responses.
# It runs in a continuous loop until the user types an exit
# command like "bye", "exit", or "quit".
# ============================================================


# ----------------------------------------------------------
# Step 1: Define the chatbot's knowledge base (responses)
# ----------------------------------------------------------
# We use a dictionary where:
#   - Each KEY is a tuple of possible user inputs (an "intent")
#   - Each VALUE is the chatbot's response for that intent
# This makes it easy to add new intents without changing logic.

responses = {
    # Intent 1: Greetings
    ("hello", "hi", "hey", "hola", "greetings"): 
        "Hello! 👋 Welcome! How can I help you today?",

    # Intent 2: Asking how the bot is doing
    ("how are you", "how are you doing", "how do you do", "whats up"): 
        "I'm just a program, but I'm running smoothly! 😄 How about you?",

    # Intent 3: Asking the bot's name / identity
    ("what is your name", "who are you", "whats your name"): 
        "I'm ChatBot v1.0 — a simple rule-based AI assistant built with Python! 🤖",

    # Intent 4: Asking what the bot can do
    ("what can you do", "help", "what do you do", "features"): 
        "I can respond to greetings, tell you about myself, share the time, "
        "tell a joke, and have a basic conversation. Try asking me something!",

    # Intent 5: Telling a joke
    ("tell me a joke", "joke", "make me laugh", "funny"): 
        "Why do programmers prefer dark mode? "
        "Because light attracts bugs! 🐛😂",

    # Intent 6: Saying thanks
    ("thank you", "thanks", "thank u", "thx"): 
        "You're welcome! Happy to help! 😊",

    # Intent 7: Asking about the weather (simple placeholder)
    ("weather", "what is the weather", "hows the weather"): 
        "I can't check live weather yet, but I hope it's sunny where you are! ☀️",

    # Intent 8: Asking about the creator
    ("who made you", "who created you", "your creator"): 
        "I was created by an aspiring AI intern as a Week 1 project! 🚀",
}

# ----------------------------------------------------------
# Step 2: Define exit commands
# ----------------------------------------------------------
# If the user types any of these words, the chatbot will
# say goodbye and stop the loop.

exit_commands = {"bye", "exit", "quit", "goodbye", "see you"}


# ----------------------------------------------------------
# Step 3: Create a function to find a matching response
# ----------------------------------------------------------
# This function takes the cleaned user input and searches
# through our responses dictionary to find a match.

def get_response(user_input):
    """
    Look up the user's input in the responses dictionary.
    
    How it works:
    - Loop through every key (tuple of keywords) in the dictionary.
    - If the user's input matches any keyword in the tuple, return
      the corresponding response.
    - If no match is found, return a fallback message.
    """
    for keywords, reply in responses.items():
        if user_input in keywords:
            return reply

    # Fallback response — returned when no intent matches
    return (
        "🤔 I'm sorry, I don't understand that yet. "
        "Try saying 'hello', 'joke', or 'help' to see what I can do!"
    )


# ----------------------------------------------------------
# Step 4: Main chat loop
# ----------------------------------------------------------
# This is the entry point of the program. It:
#   1. Greets the user
#   2. Enters a while loop that keeps asking for input
#   3. Cleans the input using lower() and strip()
#   4. Checks if the user wants to exit
#   5. Otherwise, finds and prints the matching response

def main():
    """Main function that runs the chatbot conversation loop."""
    
    # Print a welcome banner when the chatbot starts
    print("=" * 50)
    print("   🤖  Rule-Based AI Chatbot  🤖")
    print("   Type 'bye', 'exit', or 'quit' to leave.")
    print("=" * 50)
    print()

    # Continuous loop — keeps running until the user exits
    while True:
        # Get input from the user
        user_input = input("You: ")

        # Clean the input:
        #   .strip()  → removes extra spaces from both ends
        #   .lower()  → converts to lowercase for case-insensitive matching
        user_input = user_input.strip().lower()

        # Skip empty input (user just pressed Enter)
        if not user_input:
            print("ChatBot: Please type something! I'm here to chat. 💬")
            print()  # blank line for readability
            continue

        # Check if the user wants to exit
        if user_input in exit_commands:
            print("ChatBot: Goodbye! 👋 It was nice chatting with you. See you next time!")
            break  # Exit the while loop → program ends

        # Get the chatbot's response using our lookup function
        response = get_response(user_input)

        # Display the response
        print(f"ChatBot: {response}")
        print()  # blank line for readability


# ----------------------------------------------------------
# Step 5: Run the program
# ----------------------------------------------------------
# The if __name__ == "__main__" check ensures that main()
# only runs when this file is executed directly (not imported).

if __name__ == "__main__":
    main()
