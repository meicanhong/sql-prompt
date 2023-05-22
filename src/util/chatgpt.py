import os

from revChatGPT.V3 import Chatbot


class ChatGPT:

    def __init__(self, api_key: str):
        api_key = api_key if api_key else os.environ.get("API_KEY")
        self.chatbot = Chatbot(api_key=api_key)

    def ask(self, text: str):
        return self.chatbot.ask(text)

if __name__ == '__main__':
    api_key = os.environ.get("API_KEY")
    chatgpt = ChatGPT(api_key=api_key)
    print(chatgpt.ask("Hello world"))