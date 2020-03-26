from flaskapp import fapp

@fapp.route('/')
@fapp.route('/index')
def index():
    return "Hello, World!"