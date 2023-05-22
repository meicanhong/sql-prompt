import os

from revChatGPT.V3 import Chatbot

from src.conf.config import CHATGPT_CONF


class ChatGPT:

    def __init__(self):
        api_key = CHATGPT_CONF['api_key']
        self.chatbot = Chatbot(api_key=api_key)

    def ask(self, text: str):
        if len(text) > 300:
            print("ask: ", text[:300], "... \n")
        else:
            print("ask: ", text, "\n")
        result = self.chatbot.ask(text)
        print("answer: ", result, "\n")
        return result


if __name__ == '__main__':
    chatgpt = ChatGPT()
    print(chatgpt.ask("Hello world"))