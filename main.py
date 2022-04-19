import tkinter as tk
from tkinter import messagebox

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #


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
    Save the password

    Request confirmation from the user and, if confirmation is given, saves the data from the user in a .txt file

    :param website: The website that the user wants to save his credentials
    :type website: str
    :param user: The user's username/ email
    :type user: str
    :param password: The user's password
    :type password: str
    """

    is_ok = messagebox.askokcancel(
        title=website, message=f'These are the details entered: \nEmail: {user} \nPassword: {password} \nIs it ok to save?')

    if is_ok:
        with open('projects/password-manager/passwords.txt', 'a') as file:
            file.write(f'{website} | {user} | {password}\n')
            website_entry.delete(0, '')
            password_entry.delete(0, '')
            user_entry.delete(0, '')


# ---------------------------- UI SETUP ------------------------------- #
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
    text='Generate Password', command=generate_password, width=16)
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
