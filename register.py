from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
from database import Database
import hashlib
import re

# Initialize database
db = Database()
con, cur = db.get_conenction()


class RegisterWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Register - Student Management System')
        self.root.geometry('1300x700+120+50')
        self.root.config(bg='#021e2f')
        self.root.focus_force()  # Focus on this window

        # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_security_q = StringVar()
        self.var_security_a = StringVar()
        self.var_password = StringVar()
        self.var_cpassword = StringVar()
        self.var_check = IntVar()

        # Background Image
        try:
            self.bg_image = Image.open('assets/bg.png')
            self.bg_image = self.bg_image.resize((1350, 700), Image.Resampling.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(self.bg_image)
            bg_label = Label(self.root, image=self.bg_image)
            bg_label.place(x=0, y=0)
        except:
            pass

        # Main Frame
        main_frame = Frame(self.root, bg='white', bd=10, relief=RIDGE)
        main_frame.place(x=350, y=50, width=700, height=600)

        # Title
        title = Label(main_frame, text='Register Here', font=('Impact', 35, 'bold'),
                      bg='white', fg='#d77337')
        title.pack(side=TOP, fill=X)

        # Personal Information Frame
        personal_frame = LabelFrame(main_frame, text='Personal Information',
                                    font=('times new roman', 15, 'bold'),
                                    bg='white', fg='#d77337', bd=3, relief=RIDGE)
        personal_frame.place(x=20, y=100, width=650, height=120)
        personal_frame.columnconfigure(0, weight=1)
        personal_frame.columnconfigure(1, weight=1)
        personal_frame.columnconfigure(2, weight=1)
        personal_frame.columnconfigure(3, weight=1)

        # First Name
        lbl_fname = Label(personal_frame, text='First Name:',
                          font=('times new roman', 12, 'bold'), bg='white')
        lbl_fname.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        self.txt_fname = Entry(personal_frame, textvariable=self.var_fname,
                               font=('times new roman', 12), bg='#ECECEC')
        self.txt_fname.grid(row=0, column=1, padx=20, pady=10, sticky='w')

        # Last Name
        lbl_lname = Label(personal_frame, text='Last Name:',
                          font=('times new roman', 12, 'bold'), bg='white')
        lbl_lname.grid(row=0, column=2, padx=20, pady=10, sticky='w')

        self.txt_lname = Entry(personal_frame, textvariable=self.var_lname,
                               font=('times new roman', 12), bg='#ECECEC')
        self.txt_lname.grid(row=0, column=3, padx=20, pady=10, sticky='w')

        # Contact
        lbl_contact = Label(personal_frame, text='Contact No:',
                            font=('times new roman', 12, 'bold'), bg='white')
        lbl_contact.grid(row=1, column=0, padx=20, pady=10, sticky='w')

        self.txt_contact = Entry(personal_frame, textvariable=self.var_contact,
                                 font=('times new roman', 12), bg='#ECECEC')
        self.txt_contact.grid(row=1, column=1, padx=20, pady=10, sticky='w')

        # Email
        lbl_email = Label(personal_frame, text='Email:',
                          font=('times new roman', 12, 'bold'), bg='white')
        lbl_email.grid(row=1, column=2, padx=20, pady=10, sticky='w')

        self.txt_email = Entry(personal_frame, textvariable=self.var_email,
                               font=('times new roman', 12), bg='#ECECEC')
        self.txt_email.grid(row=1, column=3, padx=20, pady=10, sticky='w')

        # Security Frame
        security_frame = LabelFrame(main_frame, text='Security Information',
                                    font=('times new roman', 15, 'bold'),
                                    bg='white', fg='#d77337', bd=3, relief=RIDGE)
        security_frame.place(x=20, y=240, width=650, height=120)

        # Security Question
        lbl_security_q = Label(security_frame, text='Security Question:',
                               font=('times new roman', 12, 'bold'), bg='white')
        lbl_security_q.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        self.cmb_security_q = ttk.Combobox(security_frame, textvariable=self.var_security_q,
                                           values=('Select', 'Your Pet Name', 'Your Birth Place',
                                                   'Your Best Friend Name', 'Your Favorite Color'),
                                           font=('times new roman', 12), state='readonly')
        self.cmb_security_q.grid(row=0, column=1, padx=20, pady=10, sticky='w')
        self.cmb_security_q.current(0)

        # Security Answer
        lbl_security_a = Label(security_frame, text='Security Answer:',
                               font=('times new roman', 12, 'bold'), bg='white')
        lbl_security_a.grid(row=1, column=0, padx=20, pady=10, sticky='w')

        self.txt_security_a = Entry(security_frame, textvariable=self.var_security_a,
                                    font=('times new roman', 12), bg='#ECECEC')
        self.txt_security_a.grid(row=1, column=1, padx=20, pady=10, sticky='w')

        # Password Frame
        password_frame = LabelFrame(main_frame, text='Password Information',
                                    font=('times new roman', 15, 'bold'),
                                    bg='white', fg='#d77337', bd=3, relief=RIDGE)
        password_frame.place(x=20, y=360, width=650, height=120)


        # Password
        lbl_password = Label(password_frame, text='Password:',
                             font=('times new roman', 12, 'bold'), bg='white')
        lbl_password.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.txt_password = Entry(password_frame, textvariable=self.var_password,
                                  font=('times new roman', 12), bg='#ECECEC', show='*')
        self.txt_password.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        # Confirm Password
        lbl_cpassword = Label(password_frame, text='Confirm Password:',
                              font=('times new roman', 12, 'bold'), bg='white')
        lbl_cpassword.grid(row=0, column=2, padx=20, pady=10, sticky='w')

        self.txt_cpassword = Entry(password_frame, textvariable=self.var_cpassword,
                                   font=('times new roman', 12), bg='#ECECEC', show='*')
        self.txt_cpassword.grid(row=0, column=3, padx=20, pady=10, sticky='w')


        # Terms and Conditions
        self.chk_terms = Checkbutton(main_frame, variable=self.var_check,
                                     text='I agree to the Terms & Conditions',
                                     font=('times new roman', 12), bg='white',
                                     onvalue=1, offvalue=0)
        self.chk_terms.place(x=20, y=480)

        # Register Button
        btn_register = Button(main_frame, text='Register Now',
                              font=('times new roman', 18, 'bold'),
                              bg='#d77337', fg='white', cursor='hand2',
                              command=self.register_data)
        btn_register.place(x=50, y=520, width=180, height=40)

        # Login Button
        btn_login = Button(main_frame, text='Sign In',
                           font=('times new roman', 18, 'bold'),
                           bg='#262626', fg='white', cursor='hand2',
                           command=self.login_window)
        btn_login.place(x=250, y=520, width=180, height=40)

        # Close Button
        btn_close = Button(main_frame, text='Close',
                           font=('times new roman', 18, 'bold'),
                           bg='red', fg='white', cursor='hand2',
                           command=self.root.destroy)
        btn_close.place(x=450, y=520, width=120, height=40)

    def validate_email(self, email):
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def validate_contact(self, contact):
        """Validate contact number"""
        return len(contact) == 10 and contact.isdigit()

    def hash_password(self, password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def register_data(self):
        try:
            # Validation
            if (self.var_fname.get() == '' or self.var_lname.get() == '' or
                    self.var_contact.get() == '' or self.var_email.get() == '' or
                    self.var_security_q.get() == 'Select' or self.var_security_a.get() == '' or
                    self.var_password.get() == '' or self.var_cpassword.get() == ''):
                messagebox.showerror('Error', 'All fields are required', parent=self.root)

            elif not self.validate_email(self.var_email.get()):
                messagebox.showerror('Error', 'Invalid email format', parent=self.root)

            elif not self.validate_contact(self.var_contact.get()):
                messagebox.showerror('Error', 'Contact number must be 10 digits', parent=self.root)

            elif len(self.var_password.get()) < 6:
                messagebox.showerror('Error', 'Password must be at least 6 characters long', parent=self.root)

            elif self.var_password.get() != self.var_cpassword.get():
                messagebox.showerror('Error', 'Passwords do not match', parent=self.root)

            elif self.var_check.get() == 0:
                messagebox.showerror('Error', 'Please accept Terms & Conditions', parent=self.root)

            else:
                # Check if email already exists
                cur.execute('SELECT * FROM users WHERE email=?', (self.var_email.get(),))
                row = cur.fetchone()

                if row is not None:
                    messagebox.showerror('Error', 'Email already registered', parent=self.root)
                else:
                    # Hash password and insert data
                    hashed_password = self.hash_password(self.var_password.get())

                    cur.execute('''INSERT INTO users 
                                  (fname, lname, contact, email, security_question, security_answer, password)
                                  VALUES (?, ?, ?, ?, ?, ?, ?)''',
                                (self.var_fname.get(),
                                 self.var_lname.get(),
                                 self.var_contact.get(),
                                 self.var_email.get(),
                                 self.var_security_q.get(),
                                 self.var_security_a.get(),
                                 hashed_password))

                    con.commit()
                    messagebox.showinfo('Success', 'Registration successful! You can now login.',
                                        parent=self.root)
                    self.clear_fields()

        except Exception as e:
            messagebox.showerror('Error', f'Error due to: {str(e)}', parent=self.root)

    def clear_fields(self):
        """Clear all input fields"""
        self.var_fname.set('')
        self.var_lname.set('')
        self.var_contact.set('')
        self.var_email.set('')
        self.var_security_q.set('Select')
        self.var_security_a.set('')
        self.var_password.set('')
        self.var_cpassword.set('')
        self.var_check.set(0)

    def login_window(self):
        """Close registration and return to login"""
        self.root.destroy()


if __name__ == '__main__':
    root = Tk()
    app = RegisterWindow(root)
    root.mainloop()