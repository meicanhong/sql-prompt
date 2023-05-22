from flask import Flask

from src.prompt import Prompt

app = Flask(__name__)
prompt = Prompt()

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/ask/<question>')
def ask(question):
    return prompt.ask(question)


if __name__ == '__main__':
    app.run()
