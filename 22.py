from tkinter import *
from tkinter import messagebox

def calc(event=None):
    try:
        birth_year = int(entry_year.get())
        the_age_value = 2023 - birth_year
        age_in_month = the_age_value * 12
        age_in_weeks = age_in_month * 4
        age_in_days = the_age_value * 365

        message = (
            "Your age in months is: {}\nYour age in weeks is: {}\nYour age in days is: {}"
            .format(age_in_month, age_in_weeks, age_in_days)
        )
        messagebox.showinfo("Age Calculation Result", message)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid birth year.")

age_app = Tk()
age_app.title("Calculate Age App")
age_app.geometry("600x200")

text_label1 = Label(age_app, text="Write your Birth year", height=2, font=("Arial", 20))
text_label1.pack()

birthyear = StringVar()
birthyear.set("")
entry_year = Entry(age_app, textvariable=birthyear)
entry_year.pack()

# Bind the <Return> key to the calc function
entry_year.bind("<Return>", calc)

cal_but = Button(age_app, text="Calculate", width=8, bg="pink", fg="white", command=calc)
cal_but.pack()

age_app.mainloop()
