from flask import Flask

application = Flask(__name__)


@app.route('/')
def mainmenu():
    return 'working'

if __name__ == '__main__':
    application.run()