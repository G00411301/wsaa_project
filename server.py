#This is the main server side file in the application and contains all of the restfulAPI code

from flask import Flask, jsonify
from appDAO import appDAO

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/allbooks')
def allbooks():
    results = appDAO.getcontacts()
    return jsonify(results)


@app.route('/single/<int:id>')
def singlebook(id):
    results = appDAO.findbyid(id)
    return jsonify(results)






if __name__ == "__main__":
    app.run(debug = True)