from flask import Blueprint
from markupsafe import escape

hello_api = Blueprint('hello_api', __name__)


@hello_api.route('/hello', methods=['GET'])
def say_hello():
    return 'hello'
