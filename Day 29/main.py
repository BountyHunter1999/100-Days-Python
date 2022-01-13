from tkinter import *
from tkinter import messagebox
from password_gen import new_pwd
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_pwd():
    pwd = new_pwd()
    password_entry.delete(0, END)
    password_entry.insert(0, pwd)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_pwd():
    website = website_entry.get()
    email = email_entry.get()
    pwd = password_entry.get()

    if not website or not pwd or not email:
        messagebox.showinfo(title="Oops", message="Please don't leave any fileds empty")
    else:
        new_data = {
            website:
                {
                    'email': email,
                    'password': pwd
                }
        }
        try:
            with open("data.json", "r") as f:
                data = json.load(f)  # load json into a dict
        except FileNotFoundError:
            data = new_data
        else:
            data.update(new_data)  # update that dict if file found
        finally:
            with open("data.json", "w") as d:
                json.dump(data, d, indent=4)  # dump that dict to json

            pyperclip.copy(pwd)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# -------------------------- Search Website  -------------------------- #


def search_website():
    try:
        f = open("data.json", "r")
    except FileNotFoundError:
        messagebox.showinfo(message="File Doesn't Exist.\n Try Adding a password")
    else:
        data = json.load(f)
        website = website_entry.get()
        website_data = data.get(website)
        if website_data:
            messagebox.showinfo(message=f"Email: {website_data['email']} \nPassword: {website_data['password']}")
            print(website_data)
        else:
            messagebox.showinfo(message="No such website.")
    finally:
        f.close()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "myohmy@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)

# Buttons
web_search = Button(text="Search", width=15, command=search_website)
web_search.grid(row=1, column=2)

generate_pwd_btn = Button(text="Generate Password", width=15, command=gen_pwd)
generate_pwd_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=32, command=add_pwd)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
