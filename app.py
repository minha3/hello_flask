from flask import Flask
from hello import hello_api
app = Flask(__name__)

app.register_blueprint(hello_api)

if __name__ == '__main__':
    app.run()
