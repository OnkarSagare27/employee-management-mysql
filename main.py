from tkinter import *
from tkinter import messagebox 
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
    addButton = Button(opetionsFrame,text='Delete An Employee',height=2, width=15, padx=20, pady=20, font='lucida 10 normal')
    addButton.pack(padx=10, pady=10)
    addButton = Button(opetionsFrame, text='Update An Employee',height=2, width=15, padx=20, pady=20, font='lucida 10 normal')
    addButton.pack(padx=10, pady=10)
    addButton = Button(opetionsFrame,text='Get Details of An\nEmployee',height=2, width=15, padx=20, pady=20, font='lucida 10 normal')
    addButton.pack(padx=10, pady=10)
    addButton = Button(opetionsFrame,text='View All Employees',height=2, width=15, padx=20, pady=20, font='lucida 10 normal')
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
        if firstname and lastname and birthDate and salary and joiningDate:
            sqlClient.insertEmployee(name=f'{firstname.capitalize()} {lastname.capitalize()}', dateOfBirth=birthDate, joiningDate=joiningDate, salary=salary)
            messagebox.showwarning(title="Success", message="A new employee details added into the databse.")
            firstNameEntry.delete(0,END)
            lastNameEntry.delete(0,END)
            birthDateEntry.delete(0,END)
            joiningDateEntry.delete(0,END)
            salaryEntry.delete(0,END)
        else: 
            messagebox.showwarning(title="Error", message="All fields are required.")

    frame = Frame(window)
    frame.pack()

    userInfoFrame =LabelFrame(frame, text="Employee Information")
    userInfoFrame.grid(row= 0, column=0, padx=20, pady=10)

    firstNameLabel = Label(userInfoFrame, text="First Name")
    firstNameLabel.grid(row=0, column=0)
    lastNameLabel = Label(userInfoFrame, text="Last Name")
    lastNameLabel.grid(row=0, column=1)
    birthDateLabel = Label(userInfoFrame, text="Birth Date (yyyy-mm-dd)")
    birthDateLabel.grid(row=0, column=2)
    joiningDateLabel = Label(userInfoFrame, text="Joining Date (yyyy-mm-dd)")
    joiningDateLabel.grid(row=2, column=0)
    salaryLabel = Label(userInfoFrame, text="Salary")
    salaryLabel.grid(row=2, column=1)

    firstNameEntry = Entry(userInfoFrame)
    lastNameEntry = Entry(userInfoFrame)
    birthDateEntry = Entry(userInfoFrame)
    joiningDateEntry = Entry(userInfoFrame)
    salaryEntry = Entry(userInfoFrame)
    firstNameEntry.grid(row=1, column=0)
    lastNameEntry.grid(row=1, column=1)
    birthDateEntry.grid(row=1, column=2)
    joiningDateEntry.grid(row=3, column=0)
    salaryEntry.grid(row=3, column=1)

    for widget in userInfoFrame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    button = Button(frame, text="Save Employee Details", command= enterData)
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
    button = Button(frame, text="Cancel", command= homeScreen)
    button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

homeScreen()

window.mainloop()
