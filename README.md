# Web Services and applications module big project

This github repository contains all of the files for my submission for the big project for the web services and applications module in ATU.

The project (Type A) involved writing a flask server that would allow CRUD operations on a database via an API. The project is a contacts book that allows users to access the contacts book online and carry out basic funcitions such as create, read, update and deleting contacts from the underlying SQL data base.

## Hosting

This project is hosted on python anywhere at the below URL:


## Download

This application can be downloaded from github at the below URL:

https://github.com/G00411301/wsaa_project


## Files included in the reporitory

The following files are included in the github repository and are required in order for the application to operate.

- appDAO.py - This provides datalayer access to the application, interfacing between the API and the mySQL database
- dbconfig.py - this contains the database access credentials
- requirements.txt - details the required packages (see below)
- server.py - the flask server file
- contactcentre.html - basic html page containing AJAX and javascript to allow basic web page operation

## Python modules required

The following python modules are required in order for the application to operate

- blinker==1.8.2
- click==8.1.7
- colorama==0.4.6
- Flask==3.0.3
- Flask-Cors==4.0.1
- itsdangerous==2.2.0
- Jinja2==3.1.4
- MarkupSafe==2.1.5
- mysql-connector==2.2.9
- Werkzeug==3.0.3