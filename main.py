import tkinter.messagebox
from tkinter import *
from password_generator import PasswordGenerator
import pyperclip
import json

# CONSTANTS:
LIGHT_BLUE = '#C5EAFF'
LIGHT_RED = '#FFF2F2'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """Generates a password that has between 6 and 8 letters, 2 and 5 numbers
    in addition to 2 and 5 symbols at random"""
    passwordgenerator = PasswordGenerator()
    password_entry.delete(0, END)
    generated_password = passwordgenerator.generate_password()
    password_entry.insert(0, generated_password)
    pyperclip.copy(password_entry.get())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_entries():
    """Deletes the contents of the website and password text boxes to refocus on the website text box"""
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()


def save_info_json():
    """Saves provided info to JSON file on clicking the 'save' button"""
    new_data = {website_entry.get().title(): {"User_ID": email_entry.get(), "Password": password_entry.get()}}

    if len(website_entry.get()) < 1 or len(email_entry.get()) < 1 or len(password_entry.get()) < 1:
        tkinter.messagebox.showinfo(title='Error', message='One or more of the fields are empty!')
    else:
        confirm = tkinter.messagebox.askquestion(title='Confirm', message=f"Is the following information correct?"
                                                                          f"\nFor {website_entry.get()}"
                                                                          f"\nUser ID: {email_entry.get()}"
                                                                          f"\nPassword: {password_entry.get()}")
        if confirm == "yes":
            try:
                with open("login_data.json", "r") as login_data_json:
                    login_data = json.load(login_data_json)
            except FileNotFoundError:
                with open("login_data.json", "w") as login_data_json:
                    json.dump(new_data, login_data_json, indent=4)
            else:
                login_data.update(new_data)
                with open("login_data.json", "w") as login_data_json:
                    json.dump(login_data, login_data_json, indent=4)
            finally:
                clear_entries()

# ---------------------------- SEARCH FUNCTION ------------------------------- #


def search():
    """Search function bound to the search button, it looks for the user ID and password associated with the indicated
    website"""
    email_entry.delete(0, END)
    password_entry.delete(0, END)

    website = website_entry.get().title()
    try:
        with open("login_data.json", "r") as login_data_json:
            login_data = json.load(login_data_json)
    except FileNotFoundError:
        tkinter.messagebox.showinfo(title='Error', message="No data file found."
                                                           "Maybe you didn't save any passwords yet.")
    else:
        try:
            searched_id = login_data[website]["User_ID"]
            searched_pass = login_data[website]["Password"]
        except KeyError:
            if website_entry.get() == "":
                tkinter.messagebox.showinfo(title='Error', message='The website field is empty!')
            else:
                tkinter.messagebox.showinfo(title='Error', message=f'No details were found for {website}.')
        else:
            email_entry.insert(0, searched_id)
            password_entry.insert(0, searched_pass)
            tkinter.messagebox.showinfo(title='Found!', message=f'For {website},\n'
                                                                f'Your User ID is: {searched_id}\n'
                                                                f'Your password is: {searched_pass}')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg='white')

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
lock_logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(column=1, row=0)

# Labels:
website_label = Label(text="Website:", bg='white')
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg='white')
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg='white')
password_label.grid(column=0, row=3)

# Entries:
website_entry = Entry(width=21, bg=LIGHT_BLUE)
website_entry.place(x=97, y=200)
website_entry.focus()
email_entry = Entry(width=43, bg=LIGHT_BLUE)
email_entry.place(x=97, y=220)
password_entry = Entry(width=21, bg=LIGHT_BLUE)
password_entry.place(x=97, y=240)

# Buttons:
generate_button = Button(text='Generate Password', bg=LIGHT_RED, width=15, command=generate_password, bd=0.5)
generate_button.place(x=245, y=238)
add_button_csv = Button(text='Save', bg=LIGHT_RED, width=36, command=save_info_json, bd=2)
add_button_csv.grid(column=1, row=4, columnspan=2)
search_button = Button(text='Search', bg=LIGHT_RED, width=15, bd=0.5, command=search)
search_button.place(x=245, y=195)

window.mainloop()
