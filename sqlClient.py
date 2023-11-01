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

    def insertEmployee(self, name: str, dateOfBirth: str, joiningDate: str, department: str, salary: float):
        '''
        name: Example Name
        dateOfBirth: yyyy-mm-dd
        joiningDate: yyyy-mm-dd
        salary: 50000.00
        '''
        insertQuery = "INSERT INTO employeedetails (name, dateOfBirth, joiningDate, salary, department) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(insertQuery, (name, dateOfBirth, joiningDate, salary, department))

        self.sqlClient.commit()

    def findEmployee(self, method: str, value: str):
        '''
        method: Id/Name/Birth Date/Joining Date/Salary
        value: Value to find
        '''
        idQuery = "SELECT * FROM employeedetails WHERE id = %s"
        nameQuery = "SELECT * FROM employeeDetails WHERE name LIKE %s"
        joiningDateQuery = "SELECT * FROM employeedetails WHERE joiningDate = %s"
        birthDateQuery = "SELECT * FROM employeedetails WHERE dateOfBirth = %s"
        salaryQuery = "SELECT * FROM employeedetails WHERE salary = %s"
        
        if method == 'Id':
            self.cursor.execute(idQuery, (int(value),))
            return self.cursor.fetchall()
        elif method == 'Name':
            self.cursor.execute(nameQuery, ('%' + value + '%',))
            return self.cursor.fetchall()
        elif method == 'Birth Date':
            self.cursor.execute(birthDateQuery, (value,))
            return self.cursor.fetchall()
        elif method == 'Joining Date':
            self.cursor.execute(joiningDateQuery, (value,))
            return self.cursor.fetchall()
        else:
            self.cursor.execute(salaryQuery, (value,))
            return self.cursor.fetchall()

    def deleteEmployee(self, method: str, value: str):
        '''
        method: Id/Name/Birth Date/Joining Date/Salary
        value: Value to find and delete the employee
        '''
        idQuery = "DELETE FROM employeedetails WHERE id = %s"
        nameQuery = "DELETE FROM employeeDetails WHERE name LIKE %s"
        joiningDateQuery = "DELETE FROM employeedetails WHERE joiningDate = %s"
        birthDateQuery = "DELETE FROM employeedetails WHERE dateOfBirth = %s"
        salaryQuery = "DELETE FROM employeedetails WHERE salary = %s"

        if method == 'Id':
            self.cursor.execute(idQuery, (int(value),))
        elif method == 'Name':
            self.cursor.execute(nameQuery, ('%' + value + '%',))
        elif method == 'Birth Date':
            self.cursor.execute(birthDateQuery, (value,))
        elif method == 'Joining Date':
            self.cursor.execute(joiningDateQuery, (value,))
        else:
            self.cursor.execute(salaryQuery, (value,))

        self.sqlClient.commit()

    def updateEmployee(self, method: str, value: str, newValue: str):
        '''
        method: Id/Name/Birth Date/Joining Date/Salary
        value: Value to find the employee
        newValue: New value to update
        '''
        idQuery = "UPDATE employeedetails SET name = %s, dateOfBirth = %s, joiningDate = %s, salary = %s, department = %s WHERE id = %s"
        nameQuery = "UPDATE employeedetails SET name = %s, dateOfBirth = %s, joiningDate = %s, salary = %s, department = %s WHERE name LIKE %s"
        joiningDateQuery = "UPDATE employeedetails SET name = %s, dateOfBirth = %s, joiningDate = %s, salary = %s, department = %s WHERE joiningDate = %s"
        birthDateQuery = "UPDATE employeedetails SET name = %s, dateOfBirth = %s, joiningDate = %s, salary = %s, department = %s WHERE dateOfBirth = %s"
        salaryQuery = "UPDATE employeedetails SET name = %s, dateOfBirth = %s, joiningDate = %s, salary = %s, department = %s WHERE salary = %s"

        if method == 'Id':
            self.cursor.execute(idQuery, (newValue[1], newValue[2], newValue[3],newValue[4],newValue[5], value[0]))
        elif method == 'Name':
            self.cursor.execute(nameQuery, (newValue[1], newValue[2], newValue[3],newValue[4],newValue[5], value[1]))
        elif method == 'Birth Date':
            self.cursor.execute( birthDateQuery, (newValue[1], newValue[2], newValue[3],newValue[4],newValue[5], value[2]))
        elif method == 'Joining Date':
            self.cursor.execute(joiningDateQuery, (newValue[1], newValue[2], newValue[3],newValue[4],newValue[5], value[3]))
        else:
            self.cursor.execute(salaryQuery, (newValue[1], newValue[2], newValue[3],newValue[4], newValue[5],value[4]))

        self.sqlClient.commit()

    def getAllEmployees(self):

        query = "SELECT * FROM employeedetails"

        self.cursor.execute(query)
        return self.cursor.fetchall()