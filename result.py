from tkinter import *
from PIL import Image,ImageTk
from database import Database
from tkinter import ttk,messagebox
import sqlite3

db=Database()
con,cur=db.get_conenction()
class ResultTab:

    def __init__(self, root):
        self.root = root
        self.root.title('Student Management System')
        self.root.geometry('1200x500+250+150')
        self.root.config(bg='white')
        self.root.focus_force()
        # Variables
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()
        self.var_search=StringVar()
        # title
        title=Label(self.root,text='Add Student Results',font=('goudy old style',20,'bold'),bg='orange',fg='#262626').place(x=0,y=0,relwidth=1,height=60)
        # variables
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_total_marks=StringVar()
        self.roll_list=[]
        self.fetch_roll()
        # Widgets
        lbl_select=Label(self.root,text='Select Student',font=('goudy old style',20,'bold'),bg='white').place(x=50,y=100)
        lbl_name=Label(self.root,text='Name',font=('goudy old style',20,'bold'),bg='white').place(x=50,y=160)
        lbl_course=Label(self.root,text='Course',font=('goudy old style',20,'bold'),bg='white').place(x=50,y=220)
        lbl_marks=Label(self.root,text='Marks',font=('goudy old style',20,'bold'),bg='white').place(x=50,y=280)
        lbl_total_marks=Label(self.root,text='Total Marks',font=('goudy old style',20,'bold'),bg='white').place(x=50,y=340)

        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=('goudy old style',15,'bold'),state='readonly',justify=CENTER)
        self.txt_student.place(x=250,y=110,width=220)
        self.txt_student.set('Select')
        # Search
        self.btn_search=Button(self.root,text='Search',font=('goudy old style',15,'bold'),bg='#03a9f4',fg='white',cursor='hand2',command=self.search)
        self.btn_search.place(x=490,y=110,width=80,height=30)
        self.txt_name=Entry(self.root,textvariable=self.var_name,font=('goudy old style',15,'bold'),bg='white',state='readonly').place(x=250,y=160,width=220)
        self.txt_course=Entry(self.root,textvariable=self.var_course,font=('goudy old style',15,'bold'),bg='white',state='readonly').place(x=250,y=220,width=220)
        self.txt_marks=Entry(self.root,textvariable=self.var_marks,font=('goudy old style',15,'bold'),bg='white').place(x=250,y=280,width=220)
        self.txt_total_marks=Entry(self.root,textvariable=self.var_total_marks,font=('goudy old style',15,'bold'),bg='white').place(x=250,y=340,width=220)
        # Buttons
        self.btn_add=Button(self.root,text='Submit',font=('goudy old style',15,'bold'),bg='lightgreen',activebackground='lightgreen',cursor='hand2',command=self.add).place(x=260,y=400,height=40,width=90)
        self.btn_clear=Button(self.root,text='Clear',font=('goudy old style',15,'bold'),bg='lightgray',activebackground='lightgray',cursor='hand2',command=self.clear).place(x=370,y=400,height=40,width=90)
        # content
        self.bgImage=Image.open('assets/result.jpg')
        self.bgImage = self.bgImage.resize((500, 300), Image.Resampling.LANCZOS)
        self.bgImage=ImageTk.PhotoImage(self.bgImage)
        self.labelBg=Label(self.root,image=self.bgImage).place(x=630,y=100)

    def fetch_roll(self):
        try:
            cur.execute('select roll from students')
            rows=cur.fetchall()
            for row in rows:
                self.roll_list.append(row[0])
        except Exception as e:
            messagebox.showerror('Error',f'{str(e)}')

    def search(self):
        try:
            cur.execute("SELECT name,course FROM students WHERE roll=?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showinfo('Not Found', 'No student found with this Roll No.', parent=self.root)
        except Exception as e:
            messagebox.showerror('Error', f'Error due to: {str(e)}', parent=self.root)

    def add(self):
        try:
            if self.var_name.get() == '':
                messagebox.showerror('Error', 'Please search the student record', parent=self.root)
            else:
                # ✅ Use .get() on self.var_roll
                cur.execute('SELECT * FROM results WHERE roll=? AND course=?',
                            (self.var_roll.get(), self.var_course.get()))
                row = cur.fetchone()
                if row:
                    messagebox.showerror('Error', 'Result already present', parent=self.root)
                else:
                    marks = float(self.var_marks.get())
                    total = float(self.var_total_marks.get())
                    per = (marks * 100) / total

                    cur.execute('''
                        INSERT INTO results (roll, name, course, marks, total_marks, percentage)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_total_marks.get(),
                        f"{per:.2f}"
                    ))
                    con.commit()
                    messagebox.showinfo('Success', 'Result added successfully', parent=self.root)

        except Exception as e:
            messagebox.showerror('Error', f'{str(e)}', parent=self.root)

    def clear(self):
        self.var_roll.set('Select')
        self.var_name.set('')
        self.var_course.set('')
        self.var_marks.set('')
        self.var_total_marks.set('')


if __name__=='__main__':
    root=Tk()
    res=ResultTab(root)
    root.mainloop()
