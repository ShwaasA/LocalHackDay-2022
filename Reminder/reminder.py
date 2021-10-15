import time
import tkinter
from tkinter import messagebox

# This code is to hide the main tkinter window
root = tkinter.Tk()
root.withdraw()

task = str(input("Eevnt:\n"))
timer = float(input("Time (in minutes): "))
timer = timer
    
time.sleep(timer)
messagebox.showinfo("Reminder", f"Reminder:\n{task.upper()}")
