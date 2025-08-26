
# Task 4 - Internship Project (ApexcifyTechnologys)

import random
import datetime

# Kol EL chatbot ye2dar y3melo7

def chatbot():
    greetings = ["hi", "hello", "hey", "good morning", "good evening"]
    endings = ["bye", "exit", "quit", "stop"]
    

    jokes = [
        "Why don’t scientists trust atoms?...\n Because they make up everything! 😂",
        "I told my computer I needed a break, and it said:\n 'No problem, I’ll go to sleep.'😂😴",
        "Why was the math book sad?...\n Because it had too many problems.😂"
    ]

    quotes = [
        "Believe you can and you're halfway there. 💗",
        "Do something today that your future self will thank you for. 💗",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. 💗",
        "You can do it, just do not give up.💗"
    ]

# Elly El user yektebo7 

    print("Hi! I'm your Chatbot. \nI can tell jokes and quotes.\nTell you time and date.\n Type ( 'hello', 'time', 'joke', or 'quote') to chat with me (or 'bye' to exit).")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in greetings:
            print("Bot:", random.choice(["Hello! ", "Hi there! ", "Hey! "]))
        
        elif user_input == "how are you":
            print("Bot:", random.choice(["I'm fine, how about you? "]))

        elif user_input == "i'm fine" :
            print("Bot:", ("Good to hear that!"))
        
        elif user_input == "time":
            print("Bot: Current time is", datetime.datetime.now().strftime("%H:%M:%S"))
        
        elif user_input == "date":
            print("Bot: Today's date is", datetime.datetime.now().strftime("%Y-%m-%d"))
        
        elif user_input == "joke":
            print("Bot:", random.choice(jokes))
        
        elif user_input == "quote":
            print("Bot:", random.choice(quotes))
        
        elif user_input in endings:
            print("Bot: Goodbye! Have a wonderful day ")

        elif user_input == "thanks":
            print("Bot: Your welcome!🩷 , Feel free to ask for help. 🙈🩷🩷")
        
        else:
            print("Bot: Hmm... I don't understand you 🙉 🤔 , please! Try 'hello', 'time', 'joke', or 'quote'.")

chatbot()
