from tkinter import *

FONT = ("Arial", 15, "bold")


def converter():
    data = float(entry_kg.get())
    label_value_lbs.config(text=f"{data * 2.20462:.4f}")


window = Tk()
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

entry_kg = Entry(width=10, font=FONT)
entry_kg.grid(column=1, row=0)

label_kg = Label(text="Kg", font=FONT)
label_kg.grid(column=2, row=0)

label_iet = Label(text="is equal to", font=FONT)
label_iet.grid(column=0, row=1)

label_value_lbs = Label(font=FONT)
label_value_lbs.grid(column=1, row=1)

label_lbs = Label(text="Lbs", font=FONT)
label_lbs.grid(column=2, row=1)

button_cal = Button(text="Calculate", command=converter, font=FONT)
button_cal.grid(column=1, row=2)
button_cal.config(padx=10, pady=10)

window.mainloop()
