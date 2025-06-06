from tkinter import *
from PIL import Image,ImageTk
from database import Database
from tkinter import ttk,messagebox
import sqlite3

db=Database()
con,cur=db.get_conenction()
class ReportTab:

    def __init__(self, root):
        self.root = root
        self.root.title('Student Management System')
        self.root.geometry('1100x500+250+170')
        self.root.config(bg='white')
        self.root.focus_force()
        # variables
        self.var_search=StringVar()
        self.var_id=''
        # title
        title=Label(self.root,text='View Student Results',font=('goudy old style',20,'bold'),bg='orange',fg='#262626').place(x=0,y=0,relwidth=1,height=60)
        # Widgets
        lbl_search = Label(self.root, text='Search Student', font=('goudy old style', 20, 'bold'), bg='white')
        lbl_search.place(x=220, y=100)

        txt_search = Entry(self.root, textvariable=self.var_search, font=('goudy old style', 20, 'bold'),
                           bg='lightyellow')
        txt_search.place(x=420, y=100, width=200)

        self.btn_search = Button(self.root, text='Search', font=('goudy old style', 15, 'bold'), bg='#03a9f4',
                                 fg='white', cursor='hand2', command=self.search)
        self.btn_search.place(x=650, y=102, height=35, width=100)

        self.btn_clear = Button(self.root, text='Clear', font=('goudy old style', 15, 'bold'), bg='gray', fg='white',
                                cursor='hand2',command=self.clear)
        self.btn_clear.place(x=770, y=102, height=35, width=100)
        self.btn_delete = Button(self.root, text='Delete', font=('goudy old style', 15, 'bold'), bg='red', fg='white',
                                 cursor='hand2',command=self.delete)
        self.btn_delete.place(x=490, y=320, height=35, width=120)

        # Result Labels
        # First Row: Header Labels
        lbl_roll = Label(self.root, text='Roll No', font=('goudy old style', 15, 'bold'), bg='white', bd=2,
                         relief='groove', width=15, height=2);
        lbl_roll.place(x=100, y=170)
        lbl_name = Label(self.root, text='Name', font=('goudy old style', 15, 'bold'), bg='white', bd=2,
                         relief='groove', width=15, height=2);
        lbl_name.place(x=250, y=170)
        lbl_course = Label(self.root, text='Course', font=('goudy old style', 15, 'bold'), bg='white', bd=2,
                           relief='groove', width=15, height=2);
        lbl_course.place(x=400, y=170)
        lbl_marks = Label(self.root, text='Marks', font=('goudy old style', 15, 'bold'), bg='white', bd=2,
                          relief='groove', width=15, height=2);
        lbl_marks.place(x=550, y=170)
        lbl_total_marks = Label(self.root, text='Total Marks', font=('goudy old style', 15, 'bold'), bg='white', bd=2,
                                relief='groove', width=15, height=2);
        lbl_total_marks.place(x=700, y=170)
        lbl_per = Label(self.root, text='Percentage', font=('goudy old style', 15, 'bold'), bg='white', bd=2,
                        relief='groove', width=15, height=2);
        lbl_per.place(x=850, y=170)

        # Second Row: Data Labels
        self.roll = Label(self.root, font=('goudy old style', 15, 'bold'), bg='white', bd=2, relief='groove', width=15,
                          height=2);
        self.roll.place(x=100, y=220)
        self.name = Label(self.root, font=('goudy old style', 15, 'bold'), bg='white', bd=2, relief='groove', width=15,
                          height=2);
        self.name.place(x=250, y=220)
        self.course = Label(self.root, font=('goudy old style', 15, 'bold'), bg='white', bd=2, relief='groove',
                            width=15, height=2);
        self.course.place(x=400, y=220)
        self.marks = Label(self.root, font=('goudy old style', 15, 'bold'), bg='white', bd=2, relief='groove', width=15,
                           height=2);
        self.marks.place(x=550, y=220)
        self.total_marks = Label(self.root, font=('goudy old style', 15, 'bold'), bg='white', bd=2, relief='groove',
                                 width=15, height=2);
        self.total_marks.place(x=700, y=220)
        self.per = Label(self.root, font=('goudy old style', 15, 'bold'), bg='white', bd=2, relief='groove', width=15,
                         height=2);
        self.per.place(x=850, y=220)

    def search(self):
        try:
            if self.var_search.get() == '':
                messagebox.showerror('Error', 'Please select a student', parent=self.root)
            else:
                cur.execute("SELECT * FROM results WHERE roll=?", (self.var_search.get(),))
                row = cur.fetchone()
                if row:
                    self.var_id=row[0]
                    self.roll.config(text=row[1])  # roll
                    self.name.config(text=row[2])  # name
                    self.course.config(text=row[3])  # course
                    self.marks.config(text=row[4])  # marks
                    self.total_marks.config(text=row[5])  # total_marks
                    self.per.config(text=row[6])  # percentage
                else:
                    messagebox.showinfo('Not Found', 'No student found.', parent=self.root)

        except Exception as e:
            messagebox.showerror('Error', f'Error due to: {str(e)}', parent=self.root)

    def clear(self):
        self.var_id=''
        self.roll.config(text='')  # roll
        self.name.config(text='')  # name
        self.course.config(text='')  # course
        self.marks.config(text='')  # marks
        self.total_marks.config(text='')  # total_marks
        self.per.config(text='')  # percentage
        self.var_search.set('')

    def delete(self):
        try:
            if self.var_id=='':
                messagebox.showerror('Error','Result record required',parent=self.root)
            else:
                cur.execute('select * from results where rid=?',(self.var_id,))
                row=cur.fetchone()
                if not row:
                    messagebox.showerror('Error','Invalid Student Result',parent=self.root)
                else:
                    op=messagebox.askyesno('Confirm','Do you really want to delete this entry ?',parent=self.root)
                    if op:
                        cur.execute('delete from results where rid=?',(self.var_id,))
                        con.commit()
                        messagebox.showinfo('Delete','Result deleted successfully',parent=self.root)
                        self.clear()
        except Exception as e:
            messagebox.showerror('Error',f'{str(e)}')



if __name__=='__main__':
    root=Tk()
    rp=ReportTab(root)
    root.mainloop()
