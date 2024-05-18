#the appDAO file stores all the data access information (excluding DB access passwords etc)
#This essentially contains all of the functionality and queries required for the web app with regard to accessing data in the database


#improt the modules required. note dbconfig contains the user access details for the DB
#I added dbconfig.py to the git ignore file in order to stop the file being pushed to github as it contains the access details to the DB
import mysql.connector
import dbconfig as cfg

#create a class to handle all of the functions so we just need to import the class into the server.py file to access the DB and query it

class AppDAO:
    connection = ""
    cursor = ''
    host = ''
    user = ''
    password = ''
    database = ''

#this __init__ function sets up the relevant variables and will initialise the attributes required for the rest of the function (SQL Queries)

    def __init__(self):
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password'] 
        self.database = cfg.mysql['database'] 

#Create cursor object to store data from query results in
    def getcursor(self):
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

#Close the connection and the cursor for the DB
    def closeall(self):
        self.connection.close()
        self.cursor.close()

#select all records in my data base

    def getcontacts(self):
        cursor = self.getcursor()
        sql = "select * from contacts"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnarray = []
        for result in results:
            returnarray.append(self.convert_to_dict(result))
        #print(returnarray)
        self.closeall()
        return returnarray

    def findbyid(self, id):
        cursor = self.getcursor()
        sql = "select * from contacts where ID = %s"
        #The comma after the value in the below line caused a lot of head scratching, took some time to figure out it is required even through there is only 1 value
        val = (id,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        returnvalue = self.convert_to_dict(result)
        self.closeall()
        #print(returnvalue)
        return returnvalue
        
    def createcontact(self, contact):
        cursor = self.getcursor()
        sql = "INSERT INTO contacts (ID, Name, City, Phone, Email) VALUES (%s,%s,%s,%s,%s)"
        val = (contact.get("ID"),contact.get("Name"),contact.get("City"),contact.get("Phone"),contact.get("Email"))
        cursor.execute(sql, val)
        self.closeall()

    def convert_to_dict(self, resultLine):
        attrkeys=[
            'ID',
            'Name',
            'City',
            'Phone',
            'Email'
        ]
        contact = {}
        currentkey = 0
        for attrib in resultLine:
            contact[attrkeys[currentkey]] = attrib
            currentkey = currentkey + 1
        return contact


#This is what is imported into the server.py file to access the queries
appDAO = AppDAO()