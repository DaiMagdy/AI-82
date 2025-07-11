import random
import json

class Chatbot:
    def __init__(self,json_file):
        with open(json_file, 'r') as file:
            self.responses = json.load(file)

    def get_response(self, user_input):
        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])
        return random.choice(self.responses["default"])

if __name__ == "__main__":
    print("Chatbot: Hi! How can I assist you today?")
    bot = Chatbot("responses.json")

    while True:
        user_input = input("User: ").lower()
        response = bot.get_response(user_input)
        print("Chatbot:", response)

        if "goodbye" in user_input:
            print("Chatbot: Goodbye!")
            break