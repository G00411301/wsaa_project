#This is the main server side file in the application and contains all of the restfulAPI code

from flask import Flask
from appDAO import appDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#@app.route('/')
#def home():
#    return "Testing setup - home"






if __name__ == "__main__":
    app.run(debug = True)