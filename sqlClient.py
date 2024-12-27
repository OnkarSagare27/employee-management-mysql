import mysql.connector

class mySqlClient:
    def __init__(self, username: str, password: str, host: str, database: str):
        try:
            self.sqlClient = mysql.connector.connect(
                host=host,
                user=username,
                password=password
            )
            self.cursor = self.sqlClient.cursor()

            self.createDatabase(database)

            self.sqlClient.database = database

            self.initializeTable()
        except mysql.connector.Error as err:
            print(f"Error during initialization: {err}")
            raise

    def createDatabase(self, database: str):
        """Creates the database if it doesn't exist."""
        try:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
            print(f"Database `{database}` ensured to exist.")
        except mysql.connector.Error as err:
            print(f"Error creating database: {err}")
            raise

    def initializeTable(self):
        """Creates the `employeedetails` table if it doesn't exist."""
        try:
            createTableQuery = """
            CREATE TABLE IF NOT EXISTS employeedetails (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                dateOfBirth DATE,
                joiningDate DATE,
                salary FLOAT,
                department VARCHAR(255)
            )
            """
            self.cursor.execute(createTableQuery)
            self.sqlClient.commit()
            print("Table `employeedetails` ensured to exist.")
        except mysql.connector.Error as err:
            print(f"Error creating table: {err}")
            raise

    def insertEmployee(self, name: str, dateOfBirth: str, joiningDate: str, department: str, salary: float):
        """Inserts a new employee record into the database."""
        try:
            insertQuery = "INSERT INTO employeedetails (name, dateOfBirth, joiningDate, salary, department) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(insertQuery, (name, dateOfBirth, joiningDate, salary, department))
            self.sqlClient.commit()
            print("Employee inserted successfully.")
        except mysql.connector.Error as err:
            print(f"Error inserting employee: {err}")
            raise

    def findEmployee(self, method: str, value: str):
        """Finds employees based on the given method and value."""
        try:
            columnMap = {
                'Id': 'id',
                'Name': 'name',
                'Birth Date': 'dateOfBirth',
                'Joining Date': 'joiningDate',
                'Salary': 'salary'
            }

            if method not in columnMap:
                raise ValueError("Invalid search method.")
            query = f"SELECT * FROM employeedetails WHERE LOWER({columnMap[method]}) LIKE LOWER(%s)"
            self.cursor.execute(query, ('%' + value + '%',))
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error finding employee: {err}")
            raise

    def deleteEmployee(self, method: str, value: str):
        """Deletes employees based on the given method and value."""
        try:
            columnMap = {
                'Id': 'id',
                'Name': 'name',
                'Birth Date': 'dateOfBirth',
                'Joining Date': 'joiningDate',
                'Salary': 'salary'
            }

            if method not in columnMap:
                raise ValueError("Invalid delete method.")

            query = f"DELETE FROM employeedetails WHERE {columnMap[method]} = %s"
            self.cursor.execute(query, (value,))
            self.sqlClient.commit()
            print("Employee deleted successfully.")
        except mysql.connector.Error as err:
            print(f"Error deleting employee: {err}")
            raise

    def updateEmployee(self, updateField: str, method: str, value: str, newValue: str):
        """Updates a specific field of an employee record."""
        try:
            columnMap = {
                'Id': 'id',
                'Name': 'name',
                'Birth Date': 'dateOfBirth',
                'Joining Date': 'joiningDate',
                'Salary': 'salary',
                'Department': 'department'
            }

            if updateField not in columnMap or method not in columnMap:
                raise ValueError("Invalid updateField or method.")

            updateQuery = f"UPDATE employeedetails SET {columnMap[updateField]} = %s WHERE {columnMap[method]} = %s"
            self.cursor.execute(updateQuery, (newValue, value))
            self.sqlClient.commit()
            print("Employee updated successfully.")
        except mysql.connector.Error as err:
            print(f"Error updating employee: {err}")
            raise

    def getAllEmployees(self):
        """Fetches all employee records from the database."""
        try:
            query = "SELECT * FROM employeedetails"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error fetching employees: {err}")
            raise
