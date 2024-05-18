#This is the main server side file in the application and contains all of the restfulAPI code

from flask import Flask, jsonify, request, abort
from appDAO import appDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#here we are creating a route that returns all of the contacts in the DB as json. This will be used for two functions
# 1. when the route is called with a GET request, it will return with all of the rows in the data base, showing all of the contacts.
# 2. When the route is called with a POST request, it will create a new record in the data base
@app.route('/allcontacts', methods = ["GET", "POST"])
def allcontacts():
    if request.method == 'GET':
        results = appDAO.getcontacts()
        return jsonify(results)
    elif request.method == 'POST':
        pass
    #TODO add create record functionality

#here we are taking the id input in the URL and returng a contact with the matching ID
@app.route('/single/<int:id>')
def singlecontact(id):
    results = appDAO.findbyid(id)
    return jsonify(results)



if __name__ == "__main__":
    app.run(debug = True)