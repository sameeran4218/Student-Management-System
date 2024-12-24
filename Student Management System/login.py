from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import ttkbootstrap as ttk
from config import LOGIN_PASSWORD,LOGIN_USERNAME

# Function to handle login
def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif usernameEntry.get() == LOGIN_USERNAME and passwordEntry.get() == LOGIN_PASSWORD:
        messagebox.showinfo('Success', 'Welcome Sameeran')
        window.quit()
        window.destroy()
        import sms
    else:
        messagebox.showerror('Error', 'Please enter correct credentials')
# window
window=ttk.Window(themename='darkly')
window.geometry('1100x700+400+100')
window.title('Login')
window.resizable(False,False)

# background image
bgImage=ImageTk.PhotoImage(file='assets/bg-login.jpg')
bgLabel=Label(window,image=bgImage)
bgLabel.place(x=0,y=0)

# Login frame and logo image
loginFrame=Frame(window)
loginFrame.place(x=260,y=180)
logoImage=ImageTk.PhotoImage(file='assets/bg-logo.png')
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=30,column=0,columnspan=2,pady=10)

# username name image and input field
usernameImage=ImageTk.PhotoImage(file='assets/user.png')
usernameLabel=Label(loginFrame,image=usernameImage,text='    Username',compound=LEFT,
                    font=('times new roman',15,'bold'),bg='#F9F3D9')
usernameLabel.grid(row=35,column=0,pady=20,padx=10)
usernameEntry=Entry(loginFrame,font=('times new roman',15,'bold'),bd=5)
usernameEntry.grid(row=35,column=1,pady=20,padx=10)

# password image and entry field
passwordImage=ImageTk.PhotoImage(file='assets/lock.png')
passwordLabel=Label(loginFrame,image=passwordImage,text='    Password',compound=LEFT,
                    font=('times new roman',15,'bold'),bg='#F9F3D9')
passwordLabel.grid(row=36,column=0,pady=20,padx=20)
passwordEntry=Entry(loginFrame,font=('times new roman',15,'bold'),bd=5)
passwordEntry.grid(row=36,column=1,pady=20,padx=20)

style = ttk.Style()
style.configure('TButton',
                padding=5,
                font=('times new roman', 15, 'bold'))
# login button
loginButton = ttk.Button(loginFrame,
                         text='Login',
                         width=50,
                         cursor='hand2',
                         command=login,
                         style='TButton')
loginButton.grid(row=40, column=0, columnspan=2)

window.mainloop()