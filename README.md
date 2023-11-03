
# Employee Management System in Python (Tkinter Frontend & MySQL Backend)

**Frontend**: Tkinter based frontend.

**MySQL Integration**: Integrated MySQL as the database backend.

## Features

- **Add an Employee:** Easily add new employees to your database with this function. Input their details, and the system will store them in the database.

- **Delete an Employee:** Select the employee to delete, and with a click of a button, it will remove the employee details from the database.

- **Update an Employee:** Make changes to their information/details and save the updated data.

- **View All Employees**: Fetch all employees from the database in a single click.

## Screenshots

![App Screenshot](https://github.com/OnkarSagare27/employee-management-mysql/blob/master/screenshots/home_screeen.png)
![App Screenshot](https://github.com/OnkarSagare27/employee-management-mysql/blob/master/screenshots/add_an_employee.png)
![App Screenshot](https://github.com/OnkarSagare27/employee-management-mysql/blob/master/screenshots/delete_an_employee.png)
![App Screenshot](https://github.com/OnkarSagare27/employee-management-mysql/blob/master/screenshots/delete_an_employee_2.png)
![App Screenshot](https://github.com/OnkarSagare27/employee-management-mysql/blob/master/screenshots/update_an_employee.png)
![App Screenshot](https://github.com/OnkarSagare27/employee-management-mysql/blob/master/screenshots/update_an_employee_2.png)
![App Screenshot](https://github.com/OnkarSagare27/employee-management-mysql/blob/master/screenshots/view_all_employee.png)

## Setup
- Fork this repo
- Clone repo
```sh
git clone https://github.com/OnkarSagare27/employee-management-mysql.git
```
- Configure stuff in ``config.json``
```json
{
    "pass": "DATABASE PASSWORD",
    "user": "root",
    "host": "localhost",
    "database": "employees"
}
```
- Install requirements
```sh
pip install -r requirements.txt
```
- Run ``main.py``
```sh
python main.py
```
