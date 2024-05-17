#the appDAO file stores all the data access information (excluding DB access passwords etc)
#This essentially contains all of the functionality and queries required for the web app with regard to accessing data in the database


#improt the modules required. note dbconfig contains the user access details for the DB
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
        print(returnarray)

    def findbyid(self, ID):
        cursor = self.getcursor()
        sql = "select * from contacts where ID = %s"
        val = ID
        cursor.execute(sql, val)
        result = cursor.fetchone()
        returnvalue = self.convert_to_dict(result)
        self.closeall()
        print(returnvalue)
        return returnvalue
        


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

appDAO = AppDAO()