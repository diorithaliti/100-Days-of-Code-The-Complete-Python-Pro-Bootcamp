from flask import Flask
import random

app = Flask(__name__)



@app.route('/')
def hello_world():
    return '<h1> Welcome to the Game </h1>' \
           '<img src = "https://media.giphy.com/media/dvsgRsiCId0VjLUsSp/giphy-downsized-large.gif">' \
           '<h2> Guess the number in the url'


@app.route('/<int:number>')
def guess(number):
    if number == int(random.randint(0,2)):
        return "<img src='https://media.giphy.com/media/UXgf6pu1LlQp6CPDi0/giphy.gif'>"
    else:
        return "<img src='https://media.giphy.com/media/hPPx8yk3Bmqys/giphy-downsized-large.gif'>"

if __name__ == "__main__":
      app.run(debug= True)
