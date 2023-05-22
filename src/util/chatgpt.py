import os

from revChatGPT.V3 import Chatbot


class ChatGPT:

    def __init__(self, api_key: str = None):
        api_key = api_key if api_key else os.environ.get("API_KEY")
        self.chatbot = Chatbot(api_key=api_key)

    def ask(self, text: str):
        print("ask: ", text[:300], "\n")
        result = self.chatbot.ask(text)
        print("answer: ", result, "\n")
        return result


if __name__ == '__main__':
    api_key = os.environ.get("API_KEY")
    chatgpt = ChatGPT(api_key=api_key)
    print(chatgpt.ask("Hello world"))