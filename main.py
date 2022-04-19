import tkinter as tk
from tkinter import messagebox
import json

FONT_NAME = "Courier"

#  PASSWORD GENERATOR #


def generate():
    """
    Generates a random password

    Imports a function from another file and generates a random password
    with random letters, numbers and symbols and inserts into password field
    """

    from generator import generate_password

    password = generate_password()
    password_entry.insert(0, password)


#  SAVE PASSWORD #


def validate_inputs():
    """
    Input validation

    Validates the input given by the user
    """

    website = str(website_entry.get())
    user = str(user_entry.get())
    password = str(password_entry.get())

    if website == '' or user == '' or password == '':
        messagebox.showerror(
            title='Empty values', message='The values can not be empty')

    elif len(password) < 6:
        messagebox.showerror(
            title='Too short', message='The password is too short')

    else:
        save_password(website, user, password)


def save_password(website, user, password):
    """
    Saves the user data

    Request confirmation from the user and, if confirmation is given,
    saves the data from the user in a .txt file


    Args:
        website (str): The website that the user wants to save his credentials
        user (str): The user's username/ email
        password (str): The user's password
    """

    new_data = {
        website: {
            'email': user,
            'password': password
        }
    }

    is_ok = messagebox.askokcancel(
        title=website, message=f'These are the details entered:'
        f'\nEmail: {user}'
        f'\nPassword: {password}'
        f'\nIs it ok to save?')

    if is_ok:
        try:
            with open('projects/password-manager/data.json', 'r') as data_file:
                # Read old data
                data = json.load(data_file)

                # Update old datas with new data
                data.update(new_data)

            with open('projects/password-manager/data.json', 'w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

                messagebox.showinfo(
                    title='Success', message='Credentials stored')

        except FileNotFoundError:
            with open('projects/password-manager/data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)

                messagebox.showinfo(
                    title='Success', message='Credentials stored')


#  UI SETUP #
# Window setup
window = tk.Tk()
window.minsize(width=250, height=250)
window.title('Password manager')
window.config(padx=20, pady=20)
background_image = tk.PhotoImage(file='projects/password-manager/logo.png')

# Canvas
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
canvas.grid(column=2, row=0)
background = canvas.create_image(100, 100, image=background_image)
# background.grid(column=2, row=0)

# Form
# Labels
website_label = tk.Label(text='Website: ', font=(FONT_NAME, 12, 'normal'))
website_label.grid(column=1, row=1)

user_label = tk.Label(text='Email/ Username: ', font=(FONT_NAME, 12, 'normal'))
user_label.grid(column=1, row=2)

password_label = tk.Label(text='Password: ', font=(FONT_NAME, 12, 'normal'))
password_label.grid(column=1, row=3)

generate_password_button = tk.Button(
    text='Generate Password', command=generate, width=16)
generate_password_button.grid(column=3, row=3)

submit_button = tk.Button(text='Add', command=validate_inputs, width=46)
submit_button.grid(columnspan=3, column=2, row=4)

# Entries
website_entry = tk.Entry(width=48)
website_entry.grid(columnspan=2, column=2, row=1)
website_entry.focus()
website_entry.insert(0, 'github')

user_entry = tk.Entry(width=48)
user_entry.grid(columnspan=2, column=2, row=2)
user_entry.insert(0, 'athirsonarceus@gmail.com')

password_entry = tk.Entry(width=28)
password_entry.grid(columnspan=1, column=2, row=3)
password_entry.insert(0, 'senhabraba123')


window.mainloop()
