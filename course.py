from tkinter import *
from PIL import Image,ImageTk
from database import Database
from tkinter import ttk,messagebox
import sqlite3

db=Database()
con,cur=db.get_conenction()
class CourseTab:

    def __init__(self, root):
        self.root = root
        self.root.title('Student Management System')
        self.root.geometry('1200x600+250+150')
        self.root.config(bg='white')
        self.root.focus_force()
        # Variables
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()
        self.var_search=StringVar()
        # title
        title=Label(self.root,text='Manage Course Details',font=('goudy old style',20,'bold'),bg='#033054',fg='white').place(x=0,y=0,relwidth=1,height=60)
        # Widgets
        courseName=Label(self.root,text='Course Name',font=('goudy old style',15,'bold'),bg='white').place(x=10,y=100)
        duration=Label(self.root,text='Duration',font=('goudy old style',15,'bold'),bg='white').place(x=10,y=150)
        charges=Label(self.root,text='Charges',font=('goudy old style',15,'bold'),bg='white').place(x=10,y=200)
        description=Label(self.root,text='Description',font=('goudy old style',15,'bold'),bg='white').place(x=10,y=250)
        # Entry Fields
        self.txt_courseName=Entry(self.root,textvariable=self.var_course,font=('goudy old style',15,'bold'),bg='white')
        self.txt_courseName.place(x=150,y=100,width=200)
        txt_duration=Entry(self.root,textvariable=self.var_duration,font=('goudy old style',15,'bold'),bg='white').place(x=150,y=150,width=200)
        txt_charges=Entry(self.root,textvariable=self.var_charges,font=('goudy old style',15,'bold'),bg='white').place(x=150,y=200,width=200)
        self.txt_description=Text(self.root,font=('goudy old style',15,'bold'),bg='white')
        self.txt_description.place(x=150,y=250,width=500,height=100)
        # Buttons
        self.btn_add=Button(self.root,text='Add',font=('goudy old style',15,'bold'),bg='#2196f3',fg='white',cursor='hand2',command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text='Update',font=('goudy old style',15,'bold'),bg='#2196f3',fg='white',cursor='hand2',command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text='Delete',font=('goudy old style',15,'bold'),bg='#2196f3',fg='white',cursor='hand2',command=self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text='Clear',font=('goudy old style',15,'bold'),bg='#2196f3',fg='white',cursor='hand2',command=self.clear )
        self.btn_clear.place(x=510,y=400,width=110,height=40)

        # Search Panel
        search_course=Label(self.root,text='Course Name',font=('goudy old style',15,'bold'),bg='white').place(x=720,y=70)
        self.txt_searchcourse=Entry(self.root,textvariable=self.var_search,font=('goudy old style',15,'bold'),bg='white')
        self.txt_searchcourse.place(x=870,y=70,width=200)
        self.btn_search=Button(self.root,text='Search',font=('goudy old style',15,'bold'),bg='#2196f3',fg='white',cursor='hand2',command=self.search)
        self.btn_search.place(x=1100,y=67,width=80,height=30)
        self.btn_search_clear = Button(self.root,text='Clear Search',font=('goudy old style',15,'bold'),bg='#2196f3',fg='white',cursor='hand2',command=self.clear_search)
        self.btn_search_clear.place(x=1060,y=110,height=30)
        # Content
        self.contentFrame=Frame(self.root,bd=2,relief=RIDGE)
        self.contentFrame.place(x=720,y=150,width=450,height=370)
        scrolly=Scrollbar(self.contentFrame,orient=VERTICAL)
        scrollx=Scrollbar(self.contentFrame,orient=HORIZONTAL)
        self.courseTable=ttk.Treeview(self.contentFrame,columns=('cid','name','duration','charges','description'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.courseTable.xview)
        scrolly.config(command=self.courseTable.yview)
        self.courseTable.heading('cid',text='Course ID')
        self.courseTable.heading('name', text='Name')
        self.courseTable.heading('duration', text='Duration')
        self.courseTable.heading('charges', text='Charges')
        self.courseTable.heading('description', text='Description')
        self.courseTable['show']='headings'
        self.courseTable.column('cid',width=100)
        self.courseTable.column('name',width=100)
        self.courseTable.column('duration',width=100)
        self.courseTable.column('charges',width=100)
        self.courseTable.column('description',width=150)
        self.courseTable.pack(fill=BOTH,expand=1)
        self.courseTable.bind('<ButtonRelease-1>',self.get_Data)
        self.show()

    def get_Data(self,ev):
        r=self.courseTable.focus()
        content=self.courseTable.item(r)
        row=content['values']
        # print row
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])

    def add(self):
        try:
            if self.var_course.get()=='':
                messagebox.showerror('Error','Course name required',parent=self.root)
            else:
                cur.execute('select * from courses where name=?',(self.var_course.get(),))
                row=cur.fetchone()
                if row:
                    messagebox.showerror('Error','Course name already present',parent=self.root)
                else:
                    cur.execute('insert into courses (name,duration,charges,description) values(?,?,?,?)',
                                (self.var_course.get(),self.var_duration.get(),self.var_charges.get(),self.txt_description.get('1.0',END)))
                    con.commit()
                    messagebox.showinfo('Success','Course added successfully',parent=self.root)
                    self.show()
                    self.var_course.set('')
                    self.var_charges.set('')
                    self.var_duration.set('')
                    self.txt_description.delete('1.0', END)

        except Exception as e:
            messagebox.showerror('Error',f'{str(e)}')

    def show(self):
        try:
            cur.execute('select * from courses')
            rows=cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert('',END,values=row)
        except Exception as e:
            messagebox.showerror('Error',f'{str(e)}')

    def search(self):
        try:
            cur.execute(f"select * from courses where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert('',END,values=row)
        except Exception as e:
            messagebox.showerror('Error',f'{str(e)}')

    def clear_search(self):
        self.var_search.set('')  # Clear search field (if using Entry)
        self.show()  # Call your show() method to reload all data

    def update(self):
        try:
            if self.var_course.get()=='':
                messagebox.showerror('Error','Course name required',parent=self.root)
            else:
                cur.execute('select * from courses where name=?',(self.var_course.get(),))
                row=cur.fetchone()
                if not row:
                    messagebox.showerror('Error','Course not present',parent=self.root)
                else:
                    cur.execute('update courses set duration=?,charges=?,description=? where name=?',
                                (self.var_duration.get(),self.var_charges.get(),self.txt_description.get('1.0',END),self.var_course.get()))
                    con.commit()
                    messagebox.showinfo('Success','Course updated successfully',parent=self.root)
                    self.show()
                    self.var_course.set('')
                    self.var_charges.set('')
                    self.var_duration.set('')
                    self.txt_description.delete('1.0', END)

        except Exception as e:
            messagebox.showerror('Error',f'{str(e)}')

    def clear(self):
        self.var_search.set('')
        self.var_course.set('')
        self.var_duration.set('')
        self.var_charges.set('')
        self.txt_description.delete('1.0',END)
        self.show()

    def delete(self):
        try:
            if self.var_course.get()=='':
                messagebox.showerror('Error','Course name required',parent=self.root)
            else:
                cur.execute('select * from courses where name=?',(self.var_course.get(),))
                row=cur.fetchone()
                if not row:
                    messagebox.showerror('Error','Course not present',parent=self.root)
                else:
                    op=messagebox.askyesno('Confirm','Do you really want to delete this entry ?',parent=self.root)
                    if op:
                        cur.execute('delete from courses where name=?',(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo('Delete','Course deleted successfully',parent=self.root)
                        self.clear()
        except Exception as e:
            messagebox.showerror('Error',f'{str(e)}')



if __name__=='__main__':
    root=Tk()
    ct=CourseTab(root)
    root.mainloop()
