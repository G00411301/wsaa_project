#This is the main server side file in the application and contains all of the restfulAPI code

from flask import Flask, jsonify, request, abort
#Added th below as I was getting an error in relation to CORS on the html page: reference - https://stackoverflow.com/questions/25594893/how-to-enable-cors-in-flask
from flask_cors import CORS, cross_origin
from appDAO import appDAO

app = Flask(__name__, static_url_path='', static_folder='.')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'content-Type'

#here we are creating a route that returns all of the contacts in the DB as json. This will be used for two functions
# 1. when the route is called with a GET request, it will return with all of the rows in the data base, showing all of the contacts.
# 2. When the route is called with a POST request, it will create a new record in the data base
@app.route('/allcontacts', methods = ["GET", "POST"])
def allcontacts():
    if request.method == 'GET':
        results = appDAO.getcontacts()
        return jsonify(results)
    elif request.method == 'POST':
        contact = {
            #"ID": request.json['ID'],
            "Name": request.json['Name'],
            "City": request.json['City'],
            "Phone": request.json['Phone'],
            "Email": request.json['Email'],
        }
        addedcontact = appDAO.createcontact(contact)
        return jsonify(addedcontact)
    else:
        abort(400)

"""
Here we are taking the id input in the URL and returng a contact with the matching ID - again, depending on the HTTP method called, different fuctions are executed
Calling the function with the GET method just returns the record with the specified ID,
Calling the function with the PUT method updates a record,
Calling the function with the DELETE method deletes a record.
"""
@app.route('/single/<int:id>', methods = ["GET", "PUT", "DELETE"])
def singlecontact(id):
    if request.method == "GET":
        results = appDAO.findbyid(id)
        return jsonify(results)
    elif request.method == "PUT":
        foundcontact = appDAO.findbyid(id)
        if not foundcontact:
            abort(404)
        if not request.json:
            abort(400)
        reqjson = request.json
        if 'Name' in reqjson:
            foundcontact['Name'] = reqjson['Name']
        if 'City' in reqjson:
            foundcontact['City'] = reqjson['City']
        if 'Phone' in reqjson:
            foundcontact['Phone'] = reqjson['Phone']
        if 'Email' in reqjson:
            foundcontact['Email'] = reqjson['Email']
        appDAO.updatecontact(id, foundcontact)
        return jsonify(foundcontact)
    elif request.method == "DELETE":
        appDAO.deleteContact(id)
        return jsonify({"done":True})
    else:
        abort(400)


@app.route('/')
def home():
    return app.send_static_file("/contactcentre.html")

if __name__ == "__main__":
    app.run(debug = True)