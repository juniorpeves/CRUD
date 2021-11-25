from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola, este es mi servidor web virtual'

if __name__ == '__main__':
    app.run()