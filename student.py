from tkinter import *
from PIL import Image,ImageTk
from database import Database
from tkinter import ttk,messagebox
import sqlite3

db=Database()
con,cur=db.get_conenction()
class StudentTab:

    def __init__(self, root):
        self.root = root
        self.root.title('Student Management System')
        self.root.geometry('1200x650+250+150')
        self.root.config(bg='white')
        self.root.focus_force()
        # Variables
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_addmission=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()
        self.var_search=StringVar()

        # title
        title=Label(self.root,text='Manage Student Details',font=('goudy old style',20,'bold'),bg='#033054',fg='white').place(x=0,y=0,relwidth=1,height=60)
        # Widgets
        lbl_roll=Label(self.root,text='Roll no.',font=('goudy old style',15,'bold'),bg='white').place(x=10,y=100)
        lbl_name=Label(self.root,text='Name',font=('goudy old style',15,'bold'),bg='white').place(x=10,y=150)
        lbl_email=Label(self.root,text='Email',font=('goudy old style',15,'bold'),bg='white').place(x=10,y=200)
        lbl_gender=Label(self.root,text='Gender',font=('goudy old style',15,'bold'),bg='white').place(x=10,y=250)
        lbl_state = Label(self.root, text='State', font=('goudy old style', 15, 'bold'), bg='white').place(x=10,y=300)
        lbl_city = Label(self.root, text='City', font=('goudy old style', 15, 'bold'), bg='white').place(x=360, y=300)
        lbl_pin = Label(self.root, text='Pin', font=('goudy old style', 15, 'bold'), bg='white').place(x=530, y=300)
        lbl_address = Label(self.root, text='Address', font=('goudy old style', 15, 'bold'), bg='white').place(x=10,y=350)

        # Entry Fields
        self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=('goudy old style',15,'bold'),bg='white')
        self.txt_roll.place(x=150,y=100,width=200)
        txt_name=Entry(self.root,textvariable=self.var_name,font=('goudy old style',15,'bold'),bg='white').place(x=150,y=150,width=200)
        txt_email=Entry(self.root,textvariable=self.var_email,font=('goudy old style',15,'bold'),bg='white').place(x=150,y=200,width=200)
        self.txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=('Select','Male','Female'),font=('goudy old style',15,'bold'),state='readonly',justify=CENTER)
        self.txt_gender.place(x=150,y=250,width=200)
        self.txt_gender.current(0)
        txt_state = Entry(self.root, textvariable=self.var_state, font=('goudy old style', 15, 'bold'),bg='white').place(x=150, y=300, width=200)
        txt_city = Entry(self.root, textvariable=self.var_city, font=('goudy old style', 15, 'bold'),bg='white').place(x=410, y=300, width=100)
        txt_pin = Entry(self.root, textvariable=self.var_pin, font=('goudy old style', 15, 'bold'),bg='white').place(x=570, y=300, width=100)
        self.txt_address=Text(self.root,font=('goudy old style',15,'bold'),bg='white')
        self.txt_address.place(x=150,y=350,width=550,height=120)
        # column2
        lbl_dob=Label(self.root,text='D.O.B',font=('goudy old style',15,'bold'),bg='white').place(x=360,y=100)
        lbl_contact=Label(self.root,text='Contact',font=('goudy old style',15,'bold'),bg='white').place(x=360,y=150)
        lbl_adm=Label(self.root,text='Admission',font=('goudy old style',15,'bold'),bg='white').place(x=360,y=200)
        lbl_course=Label(self.root,text='Course',font=('goudy old style',15,'bold'),bg='white').place(x=360,y=250)

        # Entry Fields
        self.course_list=[]
        self.fetch_courses()
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=('goudy old style',15,'bold'),bg='white')
        txt_dob.place(x=460,y=100,width=200)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=('goudy old style',15,'bold'),bg='white').place(x=460,y=150,width=200)
        txt_admission=Entry(self.root,textvariable=self.var_addmission,font=('goudy old style',15,'bold'),bg='white').place(x=470,y=200,width=200)
        self.txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=('goudy old style',15,'bold'),state='readonly',justify=CENTER)
        self.txt_course.place(x=460,y=250,width=200)
        self.txt_course.set('Select')

        # Buttons
        self.btn_add=Button(self.root,text='Add',font=('goudy old style',15,'bold'),bg='#2196f3',fg='white',cursor='hand2',command=self.add)
        self.btn_add.place(x=150,y=500,width=110,height=40)
        self.btn_update=Button(self.root,text='Update',font=('goudy old style',15,'bold'),bg='#2196f3',fg='white',cursor='hand2',command=self.update)
        self.btn_update.place(x=270,y=500,width=110,height=40)
        self.btn_delete=Button(self.root,text='Delete',font=('goudy old style',15,'bold'),bg='#2196f3',fg='white',cursor='hand2',command=self.delete)
        self.btn_delete.place(x=390,y=500,width=110,height=40)
        self.btn_clear=Button(self.root,text='Clear',font=('goudy old style',15,'bold'),bg='#2196f3',fg='white',cursor='hand2',command=self.clear )
        self.btn_clear.place(x=510,y=500,width=110,height=40)
        # Search Panel
        lbl_search_roll=Label(self.root,text='Roll no.',font=('goudy old style',15,'bold'),bg='white').place(x=720,y=70)
        self.txt_search_roll=Entry(self.root,textvariable=self.var_search,font=('goudy old style',15,'bold'),bg='white')
        self.txt_search_roll.place(x=870,y=70,width=150)
        self.btn_search=Button(self.root,text='Search',font=('goudy old style',15,'bold'),bg='#2196f3',fg='white',cursor='hand2',command=self.search)
        self.btn_search_clear = Button(self.root,text='Clear Search',font=('goudy old style',15,'bold'),bg='#2196f3',fg='white',cursor='hand2',command=self.clear_search)
        self.btn_search_clear.place(x=1060,y=110,height=30)  # Adjust position as needed
        self.btn_search.place(x=1100,y=67,width=80,height=30)
        # Content
        self.contentFrame=Frame(self.root,bd=2,relief=RIDGE)
        self.contentFrame.place(x=720,y=150,width=450,height=370)
        scrolly=Scrollbar(self.contentFrame,orient=VERTICAL)
        scrollx=Scrollbar(self.contentFrame,orient=HORIZONTAL)
        self.studentTable=ttk.Treeview(self.contentFrame,columns=('roll','name','email','gender','dob','contact','admission','course','state','city','pin','address'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.studentTable.xview)
        scrolly.config(command=self.studentTable.yview)
        self.studentTable.heading('roll',text='Roll no.')
        self.studentTable.heading('name', text='Name')
        self.studentTable.heading('email', text='Email')
        self.studentTable.heading('gender', text='Gender')
        self.studentTable.heading('dob', text='D.O.B')
        self.studentTable.heading('contact', text='Contact')
        self.studentTable.heading('admission', text='Admission')
        self.studentTable.heading('course', text='Course')
        self.studentTable.heading('state', text='State')
        self.studentTable.heading('city', text='City')
        self.studentTable.heading('pin', text='Pin')
        self.studentTable.heading('address', text='Address')

        self.studentTable['show']='headings'
        self.studentTable.column('roll',width=100)
        self.studentTable.column('name',width=100)
        self.studentTable.column('email',width=100)
        self.studentTable.column('gender',width=100)
        self.studentTable.column('dob',width=100)
        self.studentTable.column('contact', width=100)
        self.studentTable.column('admission', width=100)
        self.studentTable.column('course', width=100)
        self.studentTable.column('state', width=100)
        self.studentTable.column('city', width=100)
        self.studentTable.column('pin', width=100)
        self.studentTable.column('address', width=100)
        self.studentTable.pack(fill=BOTH,expand=1)
        self.studentTable.bind('<ButtonRelease-1>',self.get_Data)
        self.show()


    def get_Data(self,ev):
        r=self.studentTable.focus()
        r = self.studentTable.focus()
        content = self.studentTable.item(r)
        row = content['values']

        # Set values to form fields
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_addmission.set(row[6])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pin.set(row[10])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[11])

    def add(self):
        try:
            if self.var_roll.get()=='':
                messagebox.showerror('Error','Roll no. required',parent=self.root)
            else:
                cur.execute('select * from students where roll=?',(self.var_roll.get(),))
                row=cur.fetchone()
                if row:
                    messagebox.showerror('Error','Roll no. already present',parent=self.root)
                else:
                    cur.execute('insert into students (roll,name,email,gender,dob,contact,admission,course,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)',
                                (self.var_roll.get(),self.var_name.get(),self.var_email.get(),self.var_gender.get(),self.var_dob.get(),self.var_contact.get(),self.var_addmission.get(),self.var_course.get(),self.var_state.get(),self.var_city.get(),self.var_pin.get(),self.txt_address.get('1.0',END)))
                    con.commit()
                    messagebox.showinfo('Success','Student added successfully',parent=self.root)
                    self.show()



        except Exception as e:
            messagebox.showerror('Error',f'{str(e)}')

    def show(self):
        try:
            cur.execute('select * from students')
            rows=cur.fetchall()
            self.studentTable.delete(*self.studentTable.get_children())
            for row in rows:
                self.studentTable.insert('',END,values=row)
        except Exception as e:
            messagebox.showerror('Error',f'{str(e)}')

    def fetch_courses(self):
        try:
            cur.execute('select name from courses')
            rows=cur.fetchall()
            for row in rows:
                self.course_list.append(row[0])
        except Exception as e:
            messagebox.showerror('Error',f'{str(e)}')

    def search(self):
        try:
            cur.execute("SELECT * FROM students WHERE roll=?", (self.var_search.get(),))
            row = cur.fetchone()
            self.studentTable.delete(*self.studentTable.get_children())  # Clear old rows
            if row:
                self.studentTable.insert('', END, values=row)
            else:
                messagebox.showinfo('Not Found', 'No student found with this Roll No.', parent=self.root)
        except Exception as e:
            messagebox.showerror('Error', f'Error due to: {str(e)}', parent=self.root)

    def clear_search(self):
        self.var_search.set('')  # Clear search field (if using Entry)
        self.show()  # Call your show() method to reload all data

    def update(self):
        try:
            if self.var_roll.get()=='':
                messagebox.showerror('Error','Roll no. required',parent=self.root)
            else:
                cur.execute('select * from students where roll=?',(self.var_roll.get(),))
                row=cur.fetchone()
                if not row:
                    messagebox.showerror('Error','Student not present',parent=self.root)
                else:
                    cur.execute('''
                        UPDATE students SET
                            name=?, email=?, gender=?, dob=?, contact=?, admission=?,
                            course=?, state=?, city=?, pin=?, address=?
                        WHERE roll=?
                    ''', (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_addmission.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get('1.0', END),
                        self.var_roll.get()
                    ))
                    con.commit()
                    messagebox.showinfo('Success', 'Student record updated successfully', parent=self.root)
                    self.show()


        except Exception as e:
            messagebox.showerror('Error',f'{str(e)}')

    def clear(self):
        self.var_roll.set('')
        self.var_name.set('')
        self.var_email.set('')
        self.var_gender.set('Select')  # if using a Combobox with default 'Select'
        self.var_dob.set('')
        self.var_contact.set('')
        self.var_addmission.set('')
        self.var_course.set('Select')  # if using Combobox or Entry
        self.var_state.set('')
        self.var_city.set('')
        self.var_pin.set('')
        self.var_search.set('')
        self.txt_address.delete('1.0', END)
        self.show()

    def delete(self):
        try:
            if self.var_roll.get()=='':
                messagebox.showerror('Error','Roll no. required',parent=self.root)
            else:
                cur.execute('select * from students where roll=?',(self.var_roll.get(),))
                row=cur.fetchone()
                if not row:
                    messagebox.showerror('Error','Student not present',parent=self.root)
                else:
                    op=messagebox.askyesno('Confirm','Do you really want to delete this entry ?',parent=self.root)
                    if op:
                        cur.execute('delete from students where roll=?',(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo('Delete','Student deleted successfully',parent=self.root)
                        self.clear()
        except Exception as e:
            messagebox.showerror('Error',f'{str(e)}')



if __name__=='__main__':
    root=Tk()
    st=StudentTab(root)
    root.mainloop()
