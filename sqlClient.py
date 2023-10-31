import mysql.connector
import json

file = open('config.json', 'r')
configData = json.load(file)

sqlClient = mysql.connector.connect(  
    host=configData['host'],
    user=configData['user'],
    password=configData['pass'],
    database=configData['database']
)

cursor = sqlClient.cursor()

def insertEmployee(name: str, dateOfBirth: str, joiningDate: str, salary, leavingData: str = None):
    '''
    name: Example Name
    dateOfBirth: yyyy-mm-dd
    joiningDate: yyyy-mm-dd
    salary: 50000.00
    '''
    insertQuery = "INSERT INTO employeedetails (name, dateOfBirth, joiningDate, leavingDate, salary) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(insertQuery, (name, dateOfBirth, joiningDate, leavingData, salary))
    sqlClient.commit()

insertEmployee("Onkar", "2004-02-27", "2023-11-01", 400.05)