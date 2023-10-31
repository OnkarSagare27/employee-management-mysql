import tkinter as tk

window = tk.Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = int(screen_width * 0.5)
window_height = int(screen_height * 0.5)

window.geometry(f"{window_width}x{window_height}")

window.title("Employee Management System")

window.mainloop()
