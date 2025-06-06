from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
from database import Database
import hashlib
from register import RegisterWindow
from forgot_password import ForgotPasswordWindow
from course import CourseTab
from student import StudentTab
from result import ResultTab
from report import ReportTab
from dashboard import ManagementSystem

# Initialize database
db = Database()
con, cur = db.get_conenction()

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Login - Student Management System')
        self.root.geometry('1300x700+120+50')
        self.root.config(bg='#021e2f')

        # Variables
        self.var_email = StringVar()
        self.var_password = StringVar()

        # Background Image
        try:
            self.bg_image = Image.open('assets/bg.png')
            self.bg_image = self.bg_image.resize((1350, 700), Image.Resampling.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(self.bg_image)
            bg_label = Label(self.root, image=self.bg_image)
            bg_label.place(x=0, y=0)
        except:
            # If background image not found, use solid color
            pass

        # Login Frame
        login_frame = Frame(self.root, bg='white', bd=10, relief=RIDGE)
        login_frame.place(x=450, y=150, width=450, height=400)

        # Title
        title = Label(login_frame, text='Login Here', font=('Impact', 35, 'bold'),
                      bg='white', fg='#d77337')
        title.pack(side=TOP, fill=X)

        # Email
        lbl_email = Label(login_frame, text='Email Address', font=('Andalus', 15, 'bold'),
                          bg='white', fg='#767171')
        lbl_email.place(x=50, y=100)

        self.txt_email = Entry(login_frame, textvariable=self.var_email,
                               font=('times new roman', 15), bg='#ECECEC')
        self.txt_email.place(x=50, y=130, width=350, height=35)

        # Password
        lbl_password = Label(login_frame, text='Password', font=('Andalus', 15, 'bold'),
                             bg='white', fg='#767171')
        lbl_password.place(x=50, y=180)

        self.txt_password = Entry(login_frame, textvariable=self.var_password,
                                  font=('times new roman', 15), bg='#ECECEC', show='*')
        self.txt_password.place(x=50, y=210, width=350, height=35)

        # Forgot Password
        forgot_btn = Button(login_frame, text='Forgot Password?', bg='white', fg='#d77337',
                            bd=0, font=('times new roman', 12), cursor='hand2',
                            command=self.forgot_password_window)
        forgot_btn.place(x=50, y=250)

        # Login Button
        login_btn = Button(login_frame, text='Login', bg='#d77337', fg='white',
                           font=('times new roman', 20, 'bold'), cursor='hand2',
                           command=self.login)
        login_btn.place(x=50, y=290, width=180, height=40)

        # Register Button
        register_btn = Button(login_frame, text='Register', bg='#262626', fg='white',
                              font=('times new roman', 20, 'bold'), cursor='hand2',
                              command=self.register_window)
        register_btn.place(x=250, y=290, width=150, height=40)

        # Bind Enter key to login
        self.root.bind('<Return>', lambda event: self.login())

        # Focus on email field
        self.txt_email.focus()

    def hash_password(self, password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self):
        try:
            if self.var_email.get() == '' or self.var_password.get() == '':
                messagebox.showerror('Error', 'All fields are required', parent=self.root)
            else:
                # Hash the entered password
                hashed_password = self.hash_password(self.var_password.get())

                # Check credentials
                cur.execute('SELECT * FROM users WHERE email=? AND password=?',
                            (self.var_email.get(), hashed_password))
                row = cur.fetchone()

                if row is None:
                    messagebox.showerror('Error', 'Invalid Email or Password', parent=self.root)
                else:
                    messagebox.showinfo('Success', f'Welcome {row[1]} {row[2]}', parent=self.root)
                    # Close login window and open main system
                    self.root.destroy()
                    self.open_main_system()

        except Exception as e:
            messagebox.showerror('Error', f'Error due to: {str(e)}', parent=self.root)

    def open_main_system(self):
        """Open the main student management system"""
        root = Tk()
        from dashboard import ManagementSystem  # Import your main system
        app = ManagementSystem(root)
        root.mainloop()

    def register_window(self):
        """Open registration window"""
        self.register_win = Toplevel(self.root)
        self.register_obj = RegisterWindow(self.register_win)

    def forgot_password_window(self):
        """Open forgot password window"""
        if self.var_email.get() == '':
            messagebox.showerror('Error', 'Please enter your email address first', parent=self.root)
        else:
            self.forgot_win = Toplevel(self.root)
            self.forgot_obj = ForgotPasswordWindow(self.forgot_win, self.var_email.get())


if __name__ == '__main__':
    root = Tk()
    app = LoginWindow(root)
    root.mainloop()



