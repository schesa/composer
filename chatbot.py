import random
import time

class Chatbot:
    def __init__(self):
        self.greetings = ["Hello!", "Hi there!", "Greetings!", "Hi! How can I help you?"]
        self.farewells = ["Goodbye!", "Bye!", "See you later!", "Take care!"]
        self.unknown_responses = [
            "I'm not sure I understand. Could you rephrase that?",
            "I'm still learning. Could you explain that differently?",
            "I don't quite get that. Can you try asking another way?"
        ]
        self.programming_responses = {
            "python": "Python is a versatile programming language known for its readability and simplicity!",
            "javascript": "JavaScript is a popular language for web development, both frontend and backend!",
            "java": "Java is a robust, object-oriented programming language used in enterprise applications!",
            "code": "I'd be happy to help you with coding! What language are you working with?",
            "docker": "Docker is a platform for developing, shipping, and running applications in containers!",
            "git": "Git is a distributed version control system for tracking changes in source code.",
            "help": """I can help you with various programming topics! Try asking about:
- Python
- JavaScript
- Java
- Docker
- Git
Or just ask about coding in general!"""
        }
        self.conversation_history = []

    def get_response(self, user_input):
        # Convert input to lowercase for easier matching
        user_input = user_input.lower().strip()
        
        # Store conversation history
        self.conversation_history.append(("user", user_input))
        
        # Simulate typing
        time.sleep(0.5)
        
        response = self._generate_response(user_input)
        
        # Store bot response
        self.conversation_history.append(("bot", response))
        return response

    def _generate_response(self, user_input):
        # Check for help command
        if user_input in ["help", "/?", "commands"]:
            return self.programming_responses["help"]

        # Check for greetings
        if any(word in user_input for word in ["hello", "hi", "hey"]):
            return random.choice(self.greetings)

        # Check for farewell
        if any(word in user_input for word in ["bye", "goodbye", "exit"]):
            return random.choice(self.farewells)

        # Check for programming-related questions
        for key in self.programming_responses:
            if key in user_input:
                return self.programming_responses[key]

        # If no specific match is found
        return random.choice(self.unknown_responses) 