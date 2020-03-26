from flask import Flask

fapp = Flask(__name__)

#from flaskapp package (defined by flaskapp folder + __init__.py), import routes which is routes.py
from flaskapp import routes
# as routes module need to import fapp defined above, putting this from flaskapp import routes in the end prevent circcular imports