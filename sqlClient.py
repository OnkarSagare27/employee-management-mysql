import mysql.connector

class mySqlClient:

    def __init__(self, username: str, password: str, host: str, database: str):
        sqlClient = mysql.connector.connect(  
            host=host,
            user=username,
            password=password,
            database=database
        )
        self.sqlClient = sqlClient
        self.cursor = sqlClient.cursor()

    def insertEmployee(self, name: str, dateOfBirth: str, joiningDate: str, salary):
        '''
        name: Example Name
        dateOfBirth: yyyy-mm-dd
        joiningDate: yyyy-mm-dd
        salary: 50000.00
        '''
        insertQuery = "INSERT INTO employeedetails (name, dateOfBirth, joiningDate, salary) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(insertQuery, (name, dateOfBirth, joiningDate, salary))
        self.sqlClient.commit()