import tkinter as tk  # tkinter is a library in python used to create GUI based applications.
from time import strftime  # Gets the current system time in a formatted way.

# Main Window

root = tk.Tk()
root.title("Python Project: Digital Clock")
root.geometry("900x450")
root.configure(bg="#1E1E1E")  # Main Window Background Color

# Date Label
label = tk.Label(root,font=("Arial", 18, "bold"),bg="#1E1E1E",fg="white")
label.pack(pady=10)

# Heading Label
label1 = tk.Label(root,text="Current Time",font=("Arial", 16),bg="#1E1E1E",fg="lightgray")
label1.pack(pady=5)

# Function to Update Date and Time
def clock():
    date = strftime("%A, %d %B %Y")
    tick = strftime("%I:%M:%S %p")
    label.config(text=date)
    label2.config(text=tick)
    label2.after(1000, clock)

# Clock Display Label
label2 = tk.Label(root,font=("Consolas", 80, "bold"),bg="black",fg="#00FF00",padx=20, pady=10)
label2.pack(pady=20)

saatvik= tk.Label(root,text="By:- Saatvik Gupta (AIML Student)",font=("Arial",12),bg="#1E1E1E",fg="gray")
saatvik.pack(pady=10,side="bottom")

internpe= tk.Label(root,text="@interpe Summer Internship (Python Programming)",font=("Arial", 12),bg="#1E1E1E",fg="gray")
internpe.pack(side="bottom", pady=10)

end = tk.Label(root,text="Built with Python & Tkinter",font=("Arial", 12),bg="#1E1E1E",fg="gray")
end.pack(side="bottom", pady=10)


clock() #Function Calling

# Start GUI
root.mainloop()