from chatbot import Chatbot
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome():
    clear_screen()
    print("🤖 Advanced Programming Assistant 🤖")
    print("Type 'bye' to exit, 'help' for commands")
    print("-" * 40)
    print("I can help you with programming-related questions!")
    print("Try asking about Python, JavaScript, Java, or coding in general.")
    print("-" * 40)

def main():
    print_welcome()
    chatbot = Chatbot()
    
    while True:
        try:
            user_input = input("\033[94mYou:\033[0m ")  # Blue color for user input
            
            if user_input.lower().strip() == "bye":
                print("\033[92mBot:\033[0m", chatbot.get_response("bye"))  # Green color for bot
                break
            elif user_input.lower().strip() == "clear":
                print_welcome()
                continue
                
            response = chatbot.get_response(user_input)
            print("\033[92mBot:\033[0m", response)  # Green color for bot
        except KeyboardInterrupt:
            print("\n\033[92mBot:\033[0m", chatbot.get_response("bye"))
            break
        except Exception as e:
            print("An error occurred:", str(e))
            break

if __name__ == "__main__":
    main() 