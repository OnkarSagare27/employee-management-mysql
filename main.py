from tkinter import *
from sqlClient import mySqlClient
import json

file = open('config.json', 'r')
configData = json.load(file)

sqlClient = mySqlClient(username=configData['user'], password=configData['pass'], host=configData['host'], database=configData['database'])

window = Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = int(screen_width * 0.7)
window_height = int(screen_height * 0.7)

window.geometry(f"{window_width}x{window_height}")

window.title("Employee Management System")

def clearScreen():
    for widget in window.winfo_children():
        widget.destroy()

button_labels = ["Add new employee","Delete an employee", "Update an employee", "Get details of an employee", "View all employees"]

frame = Frame(window, bg='grey')
addButton = Button(frame, text='Add New Employee',height=2, width=15, padx=20, pady=20, font='lucida 10 normal')
addButton.pack(padx=10, pady=10)
addButton = Button(frame,text='Delete An Employee',height=2, width=15, padx=20, pady=20, font='lucida 10 normal')
addButton.pack(padx=10, pady=10)
addButton = Button(frame, text='Update An Employee',height=2, width=15, padx=20, pady=20, font='lucida 10 normal')
addButton.pack(padx=10, pady=10)
addButton = Button(frame,text='Get Details of An\nEmployee',height=2, width=15, padx=20, pady=20, font='lucida 10 normal')
addButton.pack(padx=10, pady=10)
addButton = Button(frame,text='View All Employees',height=2, width=15, padx=20, pady=20, font='lucida 10 normal')
addButton.pack(padx=10, pady=10)
frame.pack()
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

window.mainloop()
