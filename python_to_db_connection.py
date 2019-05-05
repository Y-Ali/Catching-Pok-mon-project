import pyodbc

server = 'localhost,1433'
database = 'pokemon_db'
username = 'SA'
password = 'Passw0rd2018'

## making a connection
pokemon_db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}'+
                                 ';SERVER=' + server + ';DATABASE=' + database +
                                 ';UID=' + username + ';PWD=' + password)


# creating a cursor that can execute SQL functions on connected db
cursor = pokemon_db.cursor()
