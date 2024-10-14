from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Excited to create my first web application"

if __name__ == '__main__':
    app.run()