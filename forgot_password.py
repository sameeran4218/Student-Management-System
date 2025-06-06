from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
from database import Database
import hashlib

# Initialize database
db = Database()
con, cur = db.get_conenction()


class ForgotPasswordWindow:
    def __init__(self, root, email='', login_callback=None):
        self.root = root
        self.login_callback = login_callback
        self.root.title('Forgot Password - Student Management System')
        self.root.geometry('500x700+500+100')
        self.root.config(bg='white')
        self.root.focus_force()
        self.root.resizable(True, True)  # Allow resizing to see content

        # Variables
        self.var_email = StringVar()
        self.var_security_q = StringVar()
        self.var_security_a = StringVar()
        self.var_new_password = StringVar()
        self.var_confirm_password = StringVar()

        # Set email if provided
        if email:
            self.var_email.set(email)

        # Create scrollable frame
        self.create_scrollable_frame()

        # Create content
        self.create_content()

        # Auto-check email if provided
        if email:
            self.check_email()

    def create_scrollable_frame(self):
        """Create a scrollable frame for the content"""
        # Create canvas and scrollbar
        self.canvas = Canvas(self.root, bg='white')
        self.scrollbar = Scrollbar(self.root, orient="vertical", command=self.canvas.yview)

        # Create main frame inside canvas
        self.main_frame = Frame(self.canvas, bg='white')

        # Configure scrolling
        self.main_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Create window in canvas
        self.canvas_window = self.canvas.create_window((0, 0), window=self.main_frame, anchor="nw")

        # Configure canvas scrolling
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Pack canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True, padx=20, pady=10)
        self.scrollbar.pack(side="right", fill="y")

        # Bind mousewheel to canvas
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        self.main_frame.bind("<MouseWheel>", self._on_mousewheel)

        # Update canvas window width when canvas is resized
        self.canvas.bind('<Configure>', self._on_canvas_configure)

    def _on_canvas_configure(self, event):
        """Handle canvas resize"""
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width=canvas_width - 20)

    def _on_mousewheel(self, event):
        """Handle mouse wheel scrolling"""
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def create_content(self):
        """Create all the form content"""
        # Title
        title = Label(self.main_frame, text='Forgot Password', font=('Impact', 30, 'bold'),
                      bg='white', fg='#d77337')
        title.pack(pady=20)

        # Step 1: Email verification
        self.step1_frame = Frame(self.main_frame, bg='white')
        self.step1_frame.pack(fill=X, pady=10, padx=40)

        lbl_email = Label(self.step1_frame, text='Step 1: Email Verification',
                          font=('times new roman', 16, 'bold'), bg='white', fg='#d77337')
        lbl_email.pack(pady=(0, 10))

        lbl_email_input = Label(self.step1_frame, text='Email Address:',
                                font=('times new roman', 14, 'bold'), bg='white')
        lbl_email_input.pack()

        self.txt_email = Entry(self.step1_frame, textvariable=self.var_email,
                               font=('times new roman', 14), bg='#ECECEC', justify='center')
        self.txt_email.pack(fill=X, pady=5, ipady=5)

        btn_check_email = Button(self.step1_frame, text='Check Email',
                                 font=('times new roman', 14, 'bold'),
                                 bg='#d77337', fg='white', cursor='hand2',
                                 command=self.check_email)
        btn_check_email.pack(pady=10, ipadx=10, ipady=5)

        # Separator
        separator1 = Frame(self.main_frame, height=2, bg='#d77337')
        separator1.pack(fill=X, pady=10, padx=40)

        # Step 2: Security question (initially hidden)
        self.step2_frame = Frame(self.main_frame, bg='white')

        lbl_step2_title = Label(self.step2_frame, text='Step 2: Security Question',
                                font=('times new roman', 16, 'bold'), bg='white', fg='#d77337')
        lbl_step2_title.pack(pady=(0, 10))

        lbl_security_q = Label(self.step2_frame, text='Security Question:',
                               font=('times new roman', 14, 'bold'), bg='white')
        lbl_security_q.pack()

        self.lbl_question = Label(self.step2_frame, text='',
                                  font=('times new roman', 12), bg='white', fg='blue',
                                  wraplength=400, justify=CENTER)
        self.lbl_question.pack(pady=5, fill=X)

        lbl_security_a = Label(self.step2_frame, text='Security Answer:',
                               font=('times new roman', 14, 'bold'), bg='white')
        lbl_security_a.pack(pady=(10, 0))

        self.txt_security_a = Entry(self.step2_frame, textvariable=self.var_security_a,
                                    font=('times new roman', 14), bg='#ECECEC', justify='center')
        self.txt_security_a.pack(fill=X, pady=5, ipady=5)

        btn_check_answer = Button(self.step2_frame, text='Verify Answer',
                                  font=('times new roman', 14, 'bold'),
                                  bg='#d77337', fg='white', cursor='hand2',
                                  command=self.check_security_answer)
        btn_check_answer.pack(pady=10, ipadx=10, ipady=5)

        # Separator 2 (initially hidden)
        self.separator2 = Frame(self.main_frame, height=2, bg='green')

        # Step 3: Reset password (initially hidden)
        self.step3_frame = Frame(self.main_frame, bg='white')

        lbl_step3_title = Label(self.step3_frame, text='Step 3: Reset Password',
                                font=('times new roman', 16, 'bold'), bg='white', fg='green')
        lbl_step3_title.pack(pady=(0, 10))

        lbl_new_password = Label(self.step3_frame, text='New Password:',
                                 font=('times new roman', 14, 'bold'), bg='white')
        lbl_new_password.pack()

        self.txt_new_password = Entry(self.step3_frame, textvariable=self.var_new_password,
                                      font=('times new roman', 14), bg='#ECECEC', show='*', justify='center')
        self.txt_new_password.pack(fill=X, pady=5, ipady=5)

        lbl_confirm_password = Label(self.step3_frame, text='Confirm New Password:',
                                     font=('times new roman', 14, 'bold'), bg='white')
        lbl_confirm_password.pack(pady=(10, 0))

        self.txt_confirm_password = Entry(self.step3_frame, textvariable=self.var_confirm_password,
                                          font=('times new roman', 14), bg='#ECECEC', show='*', justify='center')
        self.txt_confirm_password.pack(fill=X, pady=5, ipady=5)

        btn_reset_password = Button(self.step3_frame, text='Reset Password',
                                    font=('times new roman', 14, 'bold'),
                                    bg='green', fg='white', cursor='hand2',
                                    command=self.reset_password)
        btn_reset_password.pack(pady=10, ipadx=10, ipady=5)

        # Back to Login Button
        btn_back = Button(self.main_frame, text='Back to Login',
                          font=('times new roman', 12, 'bold'),
                          bg='#262626', fg='white', cursor='hand2',
                          command=self.back_to_login)
        btn_back.pack(pady=20, ipadx=10, ipady=5)

    def back_to_login(self):
        """Return to login window"""
        self.root.destroy()
        if self.login_callback:
            self.login_callback()

    def hash_password(self, password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def check_email(self):
        try:
            if self.var_email.get() == '':
                messagebox.showerror('Error', 'Please enter email address', parent=self.root)
            else:
                # Check if email exists
                cur.execute('SELECT security_question FROM users WHERE email=?',
                            (self.var_email.get(),))
                row = cur.fetchone()

                if row is None:
                    messagebox.showerror('Error', 'Email not registered', parent=self.root)
                else:
                    # Show security question
                    self.lbl_question.config(text=row[0])
                    self.step2_frame.pack(fill=X, pady=10, padx=40)

                    # Update canvas scroll region
                    self.root.update_idletasks()
                    self.canvas.configure(scrollregion=self.canvas.bbox("all"))

                    messagebox.showinfo('Success', 'Email verified! Please answer the security question.',
                                        parent=self.root)
                    # Focus on security answer field
                    self.txt_security_a.focus_set()

        except Exception as e:
            messagebox.showerror('Error', f'Error due to: {str(e)}', parent=self.root)

    def check_security_answer(self):
        try:
            if self.var_security_a.get() == '':
                messagebox.showerror('Error', 'Please provide security answer', parent=self.root)
            else:
                # Check security answer
                cur.execute('SELECT security_answer FROM users WHERE email=?',
                            (self.var_email.get(),))
                row = cur.fetchone()

                if row is None:
                    messagebox.showerror('Error', 'Something went wrong', parent=self.root)
                elif row[0].lower() != self.var_security_a.get().lower():
                    messagebox.showerror('Error', 'Incorrect security answer', parent=self.root)
                else:
                    # Show separator and password reset form
                    self.separator2.pack(fill=X, pady=10, padx=40)
                    self.step3_frame.pack(fill=X, pady=10, padx=40)

                    # Update canvas scroll region and scroll to bottom
                    self.root.update_idletasks()
                    self.canvas.configure(scrollregion=self.canvas.bbox("all"))

                    # Scroll to show the reset form
                    self.canvas.yview_moveto(1.0)

                    messagebox.showinfo('Success', 'Security answer verified! You can now reset your password.',
                                        parent=self.root)
                    # Focus on new password field
                    self.txt_new_password.focus_set()

        except Exception as e:
            messagebox.showerror('Error', f'Error due to: {str(e)}', parent=self.root)

    def reset_password(self):
        try:
            if self.var_new_password.get() == '' or self.var_confirm_password.get() == '':
                messagebox.showerror('Error', 'Please fill all password fields', parent=self.root)
            elif len(self.var_new_password.get()) < 6:
                messagebox.showerror('Error', 'Password must be at least 6 characters long', parent=self.root)
            elif self.var_new_password.get() != self.var_confirm_password.get():
                messagebox.showerror('Error', 'Passwords do not match', parent=self.root)
            else:
                # Hash new password and update
                hashed_password = self.hash_password(self.var_new_password.get())

                cur.execute('UPDATE users SET password=? WHERE email=?',
                            (hashed_password, self.var_email.get()))
                con.commit()

                messagebox.showinfo('Success', 'Password reset successful! You can now login with your new password.',
                                    parent=self.root)

                # Clear all fields
                self.clear_fields()

                # Return to login window
                self.back_to_login()

        except Exception as e:
            messagebox.showerror('Error', f'Error due to: {str(e)}', parent=self.root)

    def clear_fields(self):
        """Clear all input fields"""
        self.var_email.set('')
        self.var_security_q.set('')
        self.var_security_a.set('')
        self.var_new_password.set('')
        self.var_confirm_password.set('')


if __name__ == '__main__':
    root = Tk()
    app = ForgotPasswordWindow(root)
    root.mainloop()