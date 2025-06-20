# Import necessary modules
import nltk
from nltk.chat.util import Chat, reflections

# First-time setup (uncomment if needed)
# nltk.download('punkt')

# Define interaction rules
chat_pairs = [
    [
        r"hi|hello|hey|greetings",
        ["Hey there! What can I do for you today?",]
    ],
    [
        r"my name is (.*)",
        ["Nice to meet you, %1! How may I assist you?",]
    ],
    [
        r"(.*)how are you ?",
        ["I'm good! Thanks for asking.", "Doing great, just here to help!",]
    ],
    [
        r"(.*) your name?",
        ["You can call me your digital assistant.",]
    ],
    [
        r"(.*) your age?",
        ["I don't really age, I'm always here to help.",]
    ],
    [
        r"(.*) do for me?",
        ["I can answer questions, offer suggestions, or just chat with you.",]
    ],
    [
        r"(.*) can you do?",
        ["I can help you with information or simply chat for fun.",]
    ],
    [
        r"(.*) (love|like) you", 
        ["That's sweet of you!", "Aww, thank you!", "You're awesome too!"]
    ],
    [
        r"(.*) (love|like|watch|enjoy) sports?", 
        ["I %2 football and cricket!"]
    ],
    [
        r"(.*) sports do you (love|like|watch|enjoy) ?", 
        ["I %2 cricket and football mostly!"]
    ],
    [
        r"(.*) you live?", 
        ["I'm right here in your device, always ready!"]
    ],
    [
        r"(.*) weather in (.*)?",
        ["Weather in %2 is usually nice!", "It's quite pleasant in %2.", "Pretty hot today in %2!",
         "Cool breeze blowing here in %2.", "Oops! I can't provide live weather updates for %2."]
    ],
    [
        r"(.*) (favourite|favorite) (sportsperson|player)?", 
        ["Cristiano Ronaldo is my pick.", "Virat Kohli rocks!", "MS Dhoni is legendary!",
         "Lionel Messi is amazing!", "Neymar Jr. is fun to watch!", "I admire Babar Azam!",
         "Sachin Tendulkar is iconic!", "Mbappe is lightning fast!", "Shaheen Afridi bowls great!"]
    ],
    [
        r"(.*) (help|assist)(.*)", 
        ["Of course! What do you need help with?", "I'm here to support you. Just ask!"]
    ],
    [
        r"(.*)", 
        ["Hmm... I didn't quite catch that.", "Could you say it a different way?", "Can you try rephrasing it?", 
         "I might skip that one.", "Not quite sure what you mean.", "I'd rather not respond to that."]
    ],
]

# Initialize chatbot
bot = Chat(chat_pairs, reflections)

# Chat interface
def chat():
    print("Hi! I'm your chatbot buddy. What can I do for you today?")
    print("Type 'quit' whenever you'd like to stop.")
    print()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("\nAlright, take care! See you soon.")
            break
        reply = bot.respond(user_input)
        print("\nChatbot:", reply)
        print()

# Run chatbot
if __name__ == "__main__":
    chat()
