from tkinter import *
from tkinter import messagebox 
from tkinter import ttk
from sqlClient import mySqlClient
import json

file = open('config.json', 'r')
configData = json.load(file)

sqlClient = mySqlClient(username=configData['user'], password=configData['pass'], host=configData['host'], database=configData['database'])

window = Tk()

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

windowWidth = int(screenWidth * 0.7)
windowHeight = int(screenHeight * 0.7)

window.geometry(f"{windowWidth}x{windowHeight}")

window.title("Employee Management System")

def homeScreen():
    for widget in window.winfo_children():
        widget.destroy()
    frame = Frame(window)
    frame.pack()
    opetionsFrame =LabelFrame(frame, text="Options")
    opetionsFrame.grid(row= 0, column=0, padx=20, pady=10)
    addButton = Button(opetionsFrame, text='Add New Employee',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=addScreen)
    addButton.pack(padx=10, pady=10)
    addButton = Button(opetionsFrame,text='Delete An Employee',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=deleteScreen)
    addButton.pack(padx=10, pady=10)
    addButton = Button(opetionsFrame, text='Update An Employee',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=updateScreen)
    addButton.pack(padx=10, pady=10)
    addButton = Button(opetionsFrame,text='View All Employees',height=2, width=15, padx=20, pady=20, font='lucida 10 normal', command=allEmployeeScreen)
    addButton.pack(padx=10, pady=10)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def addScreen():
    for widget in window.winfo_children():
        widget.destroy()
    def enterData():
        firstname = firstNameEntry.get()
        lastname = lastNameEntry.get()
        birthDate = birthDateEntry.get()
        joiningDate = joiningDateEntry.get()
        salary = salaryEntry.get()
        department = departmentEntry.get()
        if firstname and lastname and birthDate and salary and joiningDate and department:
            sqlClient.insertEmployee(name=f'{firstname.capitalize()} {lastname.capitalize()}', dateOfBirth=birthDate, joiningDate=joiningDate, salary=salary, department=department)
            messagebox.showwarning(title="Success", message="A new employee details added into the databse.")
            firstNameEntry.delete(0,END)
            lastNameEntry.delete(0,END)
            birthDateEntry.delete(0,END)
            joiningDateEntry.delete(0,END)
            salaryEntry.delete(0,END)
            departmentEntry.delete(0,END)
        else: 
            messagebox.showwarning(title="Error", message="All fields are required.")

    frame = Frame(window)
    frame.pack()

    employeeDetailsFrame =LabelFrame(frame, text="Add An Employee")
    employeeDetailsFrame.grid(row= 0, column=0, padx=20, pady=10)

    firstNameLabel = Label(employeeDetailsFrame, text="First Name")
    firstNameLabel.grid(row=0, column=0)
    lastNameLabel = Label(employeeDetailsFrame, text="Last Name")
    lastNameLabel.grid(row=0, column=1)
    birthDateLabel = Label(employeeDetailsFrame, text="Birth Date (yyyy-mm-dd)")
    birthDateLabel.grid(row=0, column=2)
    joiningDateLabel = Label(employeeDetailsFrame, text="Joining Date (yyyy-mm-dd)")
    joiningDateLabel.grid(row=2, column=0)
    salaryLabel = Label(employeeDetailsFrame, text="Salary")
    salaryLabel.grid(row=2, column=1)
    departmentLabel = Label(employeeDetailsFrame, text="Department")
    departmentLabel.grid(row=2, column=2)

    firstNameEntry = Entry(employeeDetailsFrame)
    lastNameEntry = Entry(employeeDetailsFrame)
    birthDateEntry = Entry(employeeDetailsFrame)
    joiningDateEntry = Entry(employeeDetailsFrame)
    salaryEntry = Entry(employeeDetailsFrame)
    departmentEntry = Entry(employeeDetailsFrame)
    firstNameEntry.grid(row=1, column=0)
    lastNameEntry.grid(row=1, column=1)
    birthDateEntry.grid(row=1, column=2)
    joiningDateEntry.grid(row=3, column=0)
    salaryEntry.grid(row=3, column=1)
    departmentEntry.grid(row=3, column=2)



    for widget in employeeDetailsFrame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    button = Button(frame, text="Save Employee Details", command= enterData)
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
    button = Button(frame, text="Cancel", command= homeScreen)
    button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def deleteScreen():
    for widget in window.winfo_children():
        widget.destroy()
    frame = Frame(window)
    frame.pack()

    findEmployeeFrame =LabelFrame(frame, text="Delete An Employee")
    findEmployeeFrame.grid(row= 0, column=0, padx=20, pady=10)
    options = [
    "Id",
    "Name",
    "Birth Date",
    "Joining Date",
    "Salary",
    ]
    usingOpt = StringVar(findEmployeeFrame)
    usingOpt.set("Find Employee Using")

    menu = OptionMenu(findEmployeeFrame, usingOpt, *options)
    menu.grid(row=0, column=0,padx=10, pady=10)

    def nextDelete():

        def find():
            def delete():
                selectedEmployee = tree.selection()
                if len(selectedEmployee) == 0:
                    messagebox.showwarning(title="Error", message="Select an employee first.")
                else:
                    for item in selectedEmployee:
                        itemValue = tree.item(item, 'values')
                        ind = 0
                        if usingOptValue == 'Id':
                            ind = 0
                        elif usingOptValue== 'Name':
                            ind = 1
                        elif usingOptValue == 'Birth Date':
                            ind = 2
                        elif usingOptValue == 'Joining Date':
                            ind = 3
                        else:
                            ind = 4
                        sqlClient.deleteEmployee(method=usingOptValue, value=itemValue[ind])
                        deleteScreen()
                        messagebox.showwarning(title="Success", message="Deleted employee details.")
            employees = sqlClient.findEmployee(method=usingOptValue, value=valueEntry.get())
            if len(employees) == 0:
                messagebox.showwarning(title="Error", message="No match found.")
            else:
                tree = ttk.Treeview(nextDeleteFrame, columns=("ID", "Name", "Date of Birth", "Joining Date", "Salary", "Department"))
                tree.heading("#0", text="", anchor="center") 
                tree.heading("ID", text="ID", anchor="center")
                tree.heading("Name", text="Name", anchor="center")
                tree.heading("Date of Birth", text="Date of Birth", anchor="center")
                tree.heading("Joining Date", text="Joining Date", anchor="center")
                tree.heading("Salary", text="Salary", anchor="center")
                tree.heading("Department", text="Department", anchor="center")

                tree.column("#0", width=0,anchor="center")
                tree.column("ID", width=50, anchor="center")
                tree.column("Name", width=200, anchor="center")
                tree.column("Date of Birth", width=100, anchor="center")
                tree.column("Joining Date", width=100, anchor="center")
                tree.column("Salary", width=100, anchor="center")
                tree.column("Department", width=100, anchor="center")
                for row in employees:
                    tree.insert("", "end", values=row)
                tree.grid(row= 4, column=0, padx=20, pady=10)
                deleteButton = Button(nextDeleteFrame, text="DELETE", command=delete)
                deleteButton.grid(row= 5, column=0, padx=20, pady=10)
        usingOptValue = usingOpt.get()
        if usingOptValue == 'Find Employee Using':
            messagebox.showwarning(title="Error", message="Select an option first.")
        else:
            for widget in window.winfo_children():
                widget.destroy()
            frame = Frame(window)
            frame.pack()

            nextDeleteFrame =LabelFrame(frame, text="Delete An Employee")
            nextDeleteFrame.grid(row= 0, column=0, padx=20, pady=10)

            valueLable = Label(nextDeleteFrame, text=f"Enter {usingOptValue}")
            valueLable.grid(row=0, column=0)
            valueEntry = Entry(nextDeleteFrame, width=100)
            valueEntry.grid(row=1, column=0,padx=10, pady=10)
            button = Button(nextDeleteFrame, text="Find", command=find)
            button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
            button = Button(nextDeleteFrame ,text="Back", command=deleteScreen)
            button.grid(row=3, column=0,sticky="news",padx=10, pady=10)
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    button = Button(findEmployeeFrame, text="Next", command=nextDelete, width=25)
    button.grid(row=1, column=0,sticky="news",padx=10, pady=10)
    button = Button(findEmployeeFrame ,text="Cancel", command=homeScreen)
    button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def updateScreen():
    for widget in window.winfo_children():
        widget.destroy()
    frame = Frame(window)
    frame.pack()

    findEmployeeFrame =LabelFrame(frame, text="Update An Employee")
    findEmployeeFrame.grid(row= 0, column=0, padx=20, pady=10)
    options = [
    "Id",
    "Name",
    "Birth Date",
    "Joining Date",
    "Salary",
    ]
    usingOpt = StringVar(findEmployeeFrame)
    usingOpt.set("Find Employee Using")

    menu = OptionMenu(findEmployeeFrame, usingOpt, *options)
    menu.grid(row=0, column=0,padx=10, pady=10)

    def nextUpdate():

        def find():
            def update():
                selectedEmployee = tree.selection()
                if len(selectedEmployee) == 0:
                    messagebox.showwarning(title="Error", message="Select an employee first.")
                else:
                    for item in selectedEmployee:
                        itemValue = tree.item(item, 'values')
                        ind = 0
                        if usingOptValue == 'Id':
                            ind = 0
                        elif usingOptValue== 'Name':
                            ind = 1
                        elif usingOptValue == 'Birth Date':
                            ind = 2
                        elif usingOptValue == 'Joining Date':
                            ind = 3
                        else:
                            ind = 4
                    for widget in window.winfo_children():
                        widget.destroy()
                    def enterData():
                        firstname = firstNameEntry.get()
                        lastname = lastNameEntry.get()
                        birthDate = birthDateEntry.get()
                        joiningDate = joiningDateEntry.get()
                        salary = salaryEntry.get()
                        department =  departmentEntry.get()
                        if firstname and lastname and birthDate and salary and joiningDate and department:
                            sqlClient.updateEmployee(method=usingOptValue, value=itemValue, newValue=(itemValue[0], f'{firstname.capitalize()} {lastname.capitalize()}', birthDate, joiningDate, salary, department))
                            messagebox.showwarning(title="Success", message="Updated Employee Details")
                            updateScreen()
                        else: 
                            messagebox.showwarning(title="Error", message="All fields are required.")

                    frame = Frame(window)
                    frame.pack()

                    employeeDetailsFrame =LabelFrame(frame, text="Update Employee Details")
                    employeeDetailsFrame.grid(row= 0, column=0, padx=20, pady=10)

                    firstNameLabel = Label(employeeDetailsFrame, text="First Name")
                    firstNameLabel.grid(row=0, column=0)
                    lastNameLabel = Label(employeeDetailsFrame, text="Last Name")
                    lastNameLabel.grid(row=0, column=1)
                    birthDateLabel = Label(employeeDetailsFrame, text="Birth Date (yyyy-mm-dd)")
                    birthDateLabel.grid(row=0, column=2)
                    joiningDateLabel = Label(employeeDetailsFrame, text="Joining Date (yyyy-mm-dd)")
                    joiningDateLabel.grid(row=2, column=0)
                    salaryLabel = Label(employeeDetailsFrame, text="Salary")
                    salaryLabel.grid(row=2, column=1)
                    departmentLabel = Label(employeeDetailsFrame, text="Department")
                    departmentLabel.grid(row=2, column=2)


                    firstNameEntry = Entry(employeeDetailsFrame)
                    firstNameEntry.insert(0,itemValue[1].split(" ")[0])
                    lastNameEntry = Entry(employeeDetailsFrame)
                    lastNameEntry.insert(0,itemValue[1].split(" ")[1])
                    birthDateEntry = Entry(employeeDetailsFrame)
                    birthDateEntry.insert(0,itemValue[2])
                    joiningDateEntry = Entry(employeeDetailsFrame)
                    joiningDateEntry.insert(0,itemValue[3])
                    salaryEntry = Entry(employeeDetailsFrame)
                    salaryEntry.insert(0,itemValue[4])
                    departmentEntry = Entry(employeeDetailsFrame)
                    departmentEntry.insert(0,itemValue[5])
                    firstNameEntry.grid(row=1, column=0)
                    lastNameEntry.grid(row=1, column=1)
                    birthDateEntry.grid(row=1, column=2)
                    joiningDateEntry.grid(row=3, column=0)
                    salaryEntry.grid(row=3, column=1)
                    departmentEntry.grid(row=3, column=2)

                    for widget in employeeDetailsFrame.winfo_children():
                        widget.grid_configure(padx=10, pady=5)

                    button = Button(frame, text="Update Employee Details", command= enterData)
                    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
                    button = Button(frame, text="Cancel", command= homeScreen)
                    button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
                    frame.place(relx=0.5, rely=0.5, anchor=CENTER)
            employees = sqlClient.findEmployee(method=usingOptValue, value=valueEntry.get())
            if len(employees) == 0:
                messagebox.showwarning(title="Error", message="No match found.")
            else:
                tree = ttk.Treeview(nextDeleteFrame, columns=("ID", "Name", "Date of Birth", "Joining Date", "Salary", "Department"))
                tree.heading("#0", text="", anchor="center") 
                tree.heading("ID", text="ID", anchor="center")
                tree.heading("Name", text="Name", anchor="center")
                tree.heading("Date of Birth", text="Date of Birth", anchor="center")
                tree.heading("Joining Date", text="Joining Date", anchor="center")
                tree.heading("Salary", text="Salary", anchor="center")
                tree.heading("Department", text="Department", anchor="center")

                tree.column("#0", width=0,anchor="center")
                tree.column("ID", width=50, anchor="center")
                tree.column("Name", width=200, anchor="center")
                tree.column("Date of Birth", width=100, anchor="center")
                tree.column("Joining Date", width=100, anchor="center")
                tree.column("Salary", width=100, anchor="center")
                tree.column("Department", width=100, anchor="center")

                for row in employees:
                    tree.insert("", "end", values=row)
                tree.grid(row= 4, column=0, padx=20, pady=10)
                deleteButton = Button(nextDeleteFrame, text="SELECT", command=update)
                deleteButton.grid(row= 5, column=0, padx=20, pady=10)
        usingOptValue = usingOpt.get()
        if usingOptValue == 'Find Employee Using':
            messagebox.showwarning(title="Error", message="Select an option first.")
        else:
            for widget in window.winfo_children():
                widget.destroy()
            frame = Frame(window)
            frame.pack()

            nextDeleteFrame =LabelFrame(frame, text="Update An Employee")
            nextDeleteFrame.grid(row= 0, column=0, padx=20, pady=10)

            valueLable = Label(nextDeleteFrame, text=f"Enter {usingOptValue}")
            valueLable.grid(row=0, column=0)
            valueEntry = Entry(nextDeleteFrame, width=100)
            valueEntry.grid(row=1, column=0,padx=10, pady=10)
            button = Button(nextDeleteFrame, text="Find", command=find)
            button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
            button = Button(nextDeleteFrame ,text="Back", command=deleteScreen)
            button.grid(row=3, column=0,sticky="news",padx=10, pady=10)
            frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    button = Button(findEmployeeFrame, text="Next", command=nextUpdate, width=25)
    button.grid(row=1, column=0,sticky="news",padx=10, pady=10)
    button = Button(findEmployeeFrame ,text="Cancel", command=homeScreen)
    button.grid(row=2, column=0,sticky="news",padx=10, pady=10)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def allEmployeeScreen():
    employees  = sqlClient.getAllEmployees()
    if len(employees) == 0:
        messagebox.showwarning(title="Error", message="No employees in the detabase.")
    else:
        for widget in window.winfo_children():
            widget.destroy()
        frame = Frame(window)
        frame.pack()

        allEmployeeFrame =LabelFrame(frame, text="Employees")
        allEmployeeFrame.grid(row= 0, column=0, padx=20, pady=10)
        tree = ttk.Treeview(allEmployeeFrame, columns=("ID", "Name", "Date of Birth", "Joining Date", "Salary", "Department"))
        tree.heading("#0", text="", anchor="center") 
        tree.heading("ID", text="ID", anchor="center")
        tree.heading("Name", text="Name", anchor="center")
        tree.heading("Date of Birth", text="Date of Birth", anchor="center")
        tree.heading("Joining Date", text="Joining Date", anchor="center")
        tree.heading("Salary", text="Salary", anchor="center")
        tree.heading("Department", text="Department", anchor="center")
        tree.column("#0", width=0,anchor="center")
        tree.column("ID", width=50, anchor="center")
        tree.column("Name", width=200, anchor="center")
        tree.column("Date of Birth", width=100, anchor="center")
        tree.column("Joining Date", width=100, anchor="center")
        tree.column("Salary", width=100, anchor="center")
        tree.column("Department", width=100, anchor="center")

        for row in employees:
            tree.insert("", "end", values=row)
        tree.grid(row= 4, column=0, padx=20, pady=10)
        deleteButton = Button(allEmployeeFrame, text="Back", command=homeScreen)
        deleteButton.grid(row= 5, column=0, padx=20, pady=10)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        
homeScreen()

window.mainloop()