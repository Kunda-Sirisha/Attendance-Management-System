from tkinter import *
from  tkinter import messagebox
import os
import csv
from datetime import datetime


file_name="attendence.csv"
if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Student ID", "Student Name", "Date","Attendance"])
def mark_attendance():
    Stud_id=entry_id.get().strip()
    Stud_name=entry_name.get().strip()
    date=entry_date.get().strip()
    attendance=attendance_var.get()
    
    if not Stud_id or not Stud_name or not date or not attendance:
        messagebox.showwarning("Input Error", "Please fill all fields!")
        return
    try:
        datetime.strptime(date, "%d-%m-%Y")
    except ValueError:
        messagebox.showwarning("Input Error", "Enter date in DD-MM-YYYY format!")
        return
    
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([Stud_id, Stud_name, date,attendance])
        messagebox.showinfo("Success","Attendance Saved Succesfully!")
    entry_id.delete(0, END)
    entry_name.delete(0, END)
    entry_date.delete(0, END)
    attendance_var.set("Present")
def view_attendance():
    view_window = Toplevel(root)
    view_window.title("Attendance Records")

    text = Text(view_window, width=60, height=20)
    text.pack()

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            text.insert(END, " | ".join(row) + "\n")
    

root = Tk()
root.title("Attendance Management System")
root.geometry("700x500")
root.config(bg="lightblue")

# ---------------- Title ----------------
title = Label(root,
              text="ATTENDANCE MANAGEMENT SYSTEM",
              font=("Arial", 18, "bold"),
              bg="navy",
              fg="white",
              pady=10)
title.pack(fill=X)

# ---------------- Form Frame ----------------
frame = Frame(root, bg="white", padx=20, pady=20)
frame.pack(pady=20)

# Student ID
Label(frame, text="Student ID:", font=("Arial", 12), bg="white").grid(row=0, column=0, sticky="w", pady=5)
entry_id = Entry(frame, width=30)
entry_id.grid(row=0, column=1)

# Student Name
Label(frame, text="Student Name:", font=("Arial", 12), bg="white").grid(row=1, column=0, sticky="w", pady=5)
entry_name = Entry(frame, width=30)
entry_name.grid(row=1, column=1)

# Date
Label(frame, text="Date:", font=("Arial", 12), bg="white").grid(row=2, column=0, sticky="w", pady=5)
entry_date = Entry(frame, width=30)
entry_date.grid(row=2, column=1)

# Attendance
Label(frame, text="Attendance:", font=("Arial", 12), bg="white").grid(row=3, column=0, sticky="w")

attendance_var = StringVar()
attendance_var.set("Present")

Radiobutton(frame,
            text="Present",
            variable=attendance_var,
            value="Present",
            bg="white").grid(row=3, column=1, sticky="w")

Radiobutton(frame,
            text="Absent",
            variable=attendance_var,
            value="Absent",
            bg="white").grid(row=4, column=1, sticky="w")

# ---------------- Buttons ----------------
button_frame = Frame(root, bg="lightblue")
button_frame.pack(pady=20)

Button(button_frame,
       text="Add Student",
       width=15).grid(row=0, column=0, padx=10)

Button(button_frame,
       text="Mark Attendance",
       width=15,
       command=mark_attendance).grid(row=0, column=1, padx=10)

Button(button_frame,
       text="View Records",
       width=15,
       command=view_attendance).grid(row=0, column=2, padx=10)

Button(button_frame,
       text="Exit",
       width=15,
       command=root.destroy).grid(row=0, column=3, padx=10)

root.mainloop()

        
    
    

    


    


