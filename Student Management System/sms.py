import time
from tkinter import *
from tkinter import messagebox,filedialog
import pymysql
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pandas as pd
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

# Functions
cursor,con=None,None
def connect_database():
    def connect():
        global cursor,con
        try:
            # Connect to the database
            con = pymysql.connect(
                host=MYSQL_HOST,
                user=MYSQL_USER,
                password=MYSQL_PASSWORD
            )
            cursor = con.cursor()
            messagebox.showinfo('Success', 'Database Connected Successfully', parent=connectWindow)
            addStudentButton.config(state=NORMAL)
            searchStudentButton.config(state=NORMAL)
            deleteStudentButton.config(state=NORMAL)
            updateStudentButton.config(state=NORMAL)
            showStudentButton.config(state=NORMAL)
            exportDataButton.config(state=NORMAL)




            # Create database if not exists
            database = MYSQL_DATABASE
            try:
                createDBQuery = f'CREATE DATABASE IF NOT EXISTS {database}'
                cursor.execute(createDBQuery)
                useDBQuery = 'USE studentmanagement'
                cursor.execute(useDBQuery)

                # Create table if not exists
                createTableQuery = (
                    'CREATE TABLE IF NOT EXISTS student('
                    'id INT NOT NULL PRIMARY KEY, '
                    'name VARCHAR(50), '
                    'mobile VARCHAR(30), '
                    'email VARCHAR(50), '
                    'gender VARCHAR(30), '
                    'address VARCHAR(50), '
                    'D_O_B VARCHAR(50))'
                )
                cursor.execute(createTableQuery)
                messagebox.showinfo('Success', 'Table Created Successfully', parent=connectWindow)

            except pymysql.MySQLError as e:
                messagebox.showerror('Error', f'Database/Table Error: {e}', parent=connectWindow)

        except pymysql.MySQLError as e:
            messagebox.showerror('Error',  'Invalid Details', parent=connectWindow)
        connectWindow.destroy()

    # window to connect to database
    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('500x300+600+200')
    connectWindow.title('Database Conenction')
    connectWindow.resizable(0,0)

    # Enter host details
    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20,pady=10)
    hostnameEntry=Entry(connectWindow,font=('roman',15,'bold'))
    hostnameEntry.grid(row=0,column=1,pady=20,padx=20)

    usernameLabel=Label(connectWindow,text='User Name',font=('arial',20,'bold'))
    usernameLabel.grid(row=1,column=0,padx=20,pady=10)
    usernameEntry=Entry(connectWindow,font=('roman',15,'bold'))
    usernameEntry.grid(row=1,column=1,pady=20,padx=20)

    passwordLabel=Label(connectWindow,text='Password',font=('arial',20,'bold'))
    passwordLabel.grid(row=2,column=0,padx=20,pady=10)
    passwordEntry=Entry(connectWindow,font=('roman',15,'bold'))
    passwordEntry.grid(row=2,column=1,pady=20,padx=20)

    connectButton=ttk.Button(connectWindow,text='Connect',command=connect)
    connectButton.grid(row=3,columnspan=4)

def exit_app():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass
def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    dataList=[]
    for index in indexing:
        content=studentTable.item(index)
        dataList.append(content['values'])
    table=pd.DataFrame(dataList,columns=['Id','Name','Mobile','Email','Gender','Address','D.O.B'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data saved successfully')

def update_student():
    def update_data():
        query = 'update student set name=%s, mobile=%s, email=%s, gender=%s, address=%s, D_O_B=%s where id=%s'
        cursor.execute(query, ( nameEntry.get(), mobileEntry.get(), emailEntry.get(), genderEntry.get(), addressEntry.get(),dobEntry.get(),idEntry.get()))
        con.commit()
        messagebox.showinfo('Success', 'Entry has been updated')
        update_window.destroy()
        show_student()

    # Update window layout
    update_window = Toplevel()
    update_window.grab_set()
    update_window.resizable(0, 0)
    update_window.geometry('650x600+50+20')

    # Labels and Entries for student data to update
    idLabel = Label(update_window, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=20, pady=15, sticky=W)
    idEntry = Entry(update_window, font=('times new roman', 20, 'bold'), width=25)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(update_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=20, pady=15, sticky=W)
    nameEntry = Entry(update_window, font=('times new roman', 20, 'bold'), width=25)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    mobileLabel = Label(update_window, text='Mobile', font=('times new roman', 20, 'bold'))
    mobileLabel.grid(row=2, column=0, padx=20, pady=15, sticky=W)
    mobileEntry = Entry(update_window, font=('times new roman', 20, 'bold'), width=25)
    mobileEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(update_window, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=20, pady=15, sticky=W)
    emailEntry = Entry(update_window, font=('times new roman', 20, 'bold'), width=25)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    genderLabel = Label(update_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=4, column=0, padx=20, pady=15, sticky=W)
    genderEntry = Entry(update_window, font=('times new roman', 20, 'bold'), width=25)
    genderEntry.grid(row=4, column=1, pady=15, padx=10)

    addressLabel = Label(update_window, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=5, column=0, padx=20, pady=15, sticky=W)
    addressEntry = Entry(update_window, font=('times new roman', 20, 'bold'), width=25)
    addressEntry.grid(row=5, column=1, pady=15, padx=10)

    dobLabel = Label(update_window, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=20, pady=15, sticky=W)
    dobEntry = Entry(update_window, font=('times new roman', 20, 'bold'), width=25)
    dobEntry.grid(row=6, column=1, pady=15, padx=10)

    # Update Button
    update_studentButton = ttk.Button(update_window, text='Update Student', command=update_data)
    update_studentButton.grid(row=7, columnspan=2, pady=20)

    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    listdata=content['values']
    idEntry.insert(0,listdata[0])
    nameEntry.insert(0, listdata[1])
    mobileEntry.insert(0, listdata[2])
    emailEntry.insert(0, listdata[3])
    genderEntry.insert(0, listdata[4])
    addressEntry.insert(0, listdata[5])
    dobEntry.insert(0, listdata[6])

def show_student():
    query='select * from student'
    cursor.execute(query)
    fetched_data=cursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)

def search_student():
    def search_data():
        # Start with a basic query
        query = 'SELECT * FROM student WHERE 1=1'
        params = []

        # Only add conditions for non-empty fields
        if idEntry.get():
            query += ' AND id=%s'
            params.append(idEntry.get())
        if nameEntry.get():
            query += ' AND name=%s'
            params.append(nameEntry.get())
        if mobileEntry.get():
            query += ' AND mobile=%s'
            params.append(mobileEntry.get())
        if emailEntry.get():
            query += ' AND email=%s'
            params.append(emailEntry.get())
        if genderEntry.get():
            query += ' AND gender=%s'
            params.append(genderEntry.get())
        if addressEntry.get():
            query += ' AND address=%s'
            params.append(addressEntry.get())
        if dobEntry.get():
                query += ' AND D_O_B=%s'
                params.append(dobEntry.get())

        # Execute the query with the constructed parameters
        try:
            cursor.execute(query, tuple(params))
            fetched_data = cursor.fetchall()

            # Clear previous search results
            studentTable.delete(*studentTable.get_children())

            if not fetched_data:
                messagebox.showinfo('No Results', 'No matching records found.')
            else:
                for data in fetched_data:
                    studentTable.insert('', END, values=data)
        except Exception as e:
            messagebox.showerror('Error', f'Error executing query: {e}')

    search_window = Toplevel()
    search_window.grab_set()
    search_window.resizable(0, 0)
    search_window.geometry('650x600+50+20')

    # Labels and Entries for search criteria
    idLabel = Label(search_window, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=20, pady=15, sticky=W)
    idEntry = Entry(search_window, font=('times new roman', 20, 'bold'), width=25)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(search_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=20, pady=15, sticky=W)
    nameEntry = Entry(search_window, font=('times new roman', 20, 'bold'), width=25)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    mobileLabel = Label(search_window, text='Mobile', font=('times new roman', 20, 'bold'))
    mobileLabel.grid(row=2, column=0, padx=20, pady=15, sticky=W)
    mobileEntry = Entry(search_window, font=('times new roman', 20, 'bold'), width=25)
    mobileEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(search_window, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=20, pady=15, sticky=W)
    emailEntry = Entry(search_window, font=('times new roman', 20, 'bold'), width=25)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    genderLabel = Label(search_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=4, column=0, padx=20, pady=15, sticky=W)
    genderEntry = Entry(search_window, font=('times new roman', 20, 'bold'), width=25)
    genderEntry.grid(row=4, column=1, pady=15, padx=10)

    addressLabel = Label(search_window, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=5, column=0, padx=20, pady=15, sticky=W)
    addressEntry = Entry(search_window, font=('times new roman', 20, 'bold'), width=25)
    addressEntry.grid(row=5, column=1, pady=15, padx=10)

    dobLabel = Label(search_window, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=20, pady=15, sticky=W)
    dobEntry = Entry(search_window, font=('times new roman', 20, 'bold'), width=25)
    dobEntry.grid(row=6, column=1, pady=15, padx=10)

    search_studentButton = ttk.Button(search_window, text='Search Student', command=search_data)
    search_studentButton.grid(row=7, columnspan=2, pady=20)

def add_student():
    def add_data():
        global cursor, con
        if idEntry.get() == '' or nameEntry.get() == '' or mobileEntry.get() == '' or emailEntry.get() == '' or genderEntry.get() == '' or addressEntry.get() == '' or dobEntry.get() == '':
            messagebox.showerror('Error', 'All fields are required', parent=add_window)
        else:
            query = 'insert into student values(%s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(query, (
            idEntry.get(), nameEntry.get(), mobileEntry.get(), emailEntry.get(), genderEntry.get(), addressEntry.get(),
            dobEntry.get()))
            con.commit()
            messagebox.showinfo('Success', 'Data added successfully')
            # Clear the input fields
            idEntry.delete(0, END)
            nameEntry.delete(0, END)
            mobileEntry.delete(0, END)
            emailEntry.delete(0, END)
            genderEntry.delete(0, END)
            addressEntry.delete(0, END)
            dobEntry.delete(0, END)

            # Refresh the student table
            query = 'select * from student'
            cursor.execute(query)
            fetched_data = cursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in fetched_data:
                studentTable.insert('', END, values=data)

    add_window=Toplevel()
    add_window.grab_set()
    add_window.resizable(0,0)
    add_window.geometry('650x600+50+20')
    idLabel=Label(add_window,text='Id',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=20,pady=15,sticky=W)
    idEntry=Entry(add_window,font=('times new roman',20,'bold'),width=25)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    nameLabel=Label(add_window,text='Name',font=('times new roman',20,'bold'))
    nameLabel.grid(row=1,column=0,padx=20,pady=15,sticky=W)
    nameEntry=Entry(add_window,font=('times new roman',20,'bold'),width=25)
    nameEntry.grid(row=1,column=1,pady=15,padx=10)

    mobileLabel=Label(add_window,text='Mobile',font=('times new roman',20,'bold'))
    mobileLabel.grid(row=2,column=0,padx=20,pady=15,sticky=W)
    mobileEntry=Entry(add_window,font=('times new roman',20,'bold'),width=25)
    mobileEntry.grid(row=2,column=1,pady=15,padx=10)

    emailLabel=Label(add_window,text='Email',font=('times new roman',20,'bold'))
    emailLabel.grid(row=3,column=0,padx=20,pady=15,sticky=W)
    emailEntry=Entry(add_window,font=('times new roman',20,'bold'),width=25)
    emailEntry.grid(row=3,column=1,pady=15,padx=10)

    genderLabel=Label(add_window,text='Gender',font=('times new roman',20,'bold'))
    genderLabel.grid(row=4,column=0,padx=20,pady=15,sticky=W)
    genderEntry=Entry(add_window,font=('times new roman',20,'bold'),width=25)
    genderEntry.grid(row=4,column=1,pady=15,padx=10)

    addressLabel=Label(add_window,text='Address',font=('times new roman',20,'bold'))
    addressLabel.grid(row=5,column=0,padx=20,pady=15,sticky=W)
    addressEntry=Entry(add_window,font=('times new roman',20,'bold'),width=25)
    addressEntry.grid(row=5,column=1,pady=15,padx=10)

    dobLabel=Label(add_window,text='D.O.B',font=('times new roman',20,'bold'))
    dobLabel.grid(row=6,column=0,padx=20,pady=15,sticky=W)
    dobEntry=Entry(add_window,font=('times new roman',20,'bold'),width=25)
    dobEntry.grid(row=6,column=1,pady=15,padx=10)

    add_studentButton=ttk.Button(add_window,text='Add Student',command=add_data)
    add_studentButton.grid(row=7,columnspan=2,pady=20)

def delete_student():
    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    cursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted','The entry has been deleted')
    query='select * from student'
    cursor.execute(query)
    fetched_data=cursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)

def clock():
    date=time.strftime('%d/%m/%y')
    currTime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'Date: {date}\nTime: {currTime}')
    datetimeLabel.after(1000,clock)

i,text=0,''
def slider():
    global text,i
    if i==len(s):
        i=0
        text=''
    text+=s[i]
    i+=1
    sliderLabel.config(text=text)
    sliderLabel.after(150,slider)

# GUI
root=ttk.Window(themename='darkly')
root.geometry('1500x800+200+100')
root.title('Home')
root.resizable(0,0)

# Top Frame
# Date & Time
datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=20,y=5)
clock()

# Title label
s='Student Management System'
sliderLabel=Label(root,font=('arial',30,'italic bold'),text=s)
sliderLabel.place(x=400,y=0)
slider()

# Connect Database button
connectButton=ttk.Button(root, text='Connect Database', width=30,cursor='hand2',command=connect_database)
connectButton.place(x=1150,y=20)

# Left Frame
leftFrame=Frame(root)
leftFrame.place(x=100,y=100,width=350,height=700)

# Logo Image
logoImage=PhotoImage(file='assets/graduated.png')
logoLabel=Label(leftFrame,image=logoImage)
logoLabel.grid(row=0,column=0)

# Add Student Button
addStudentButton=ttk.Button(leftFrame,text='Add Student',width=30,cursor='hand2',state=DISABLED,command=add_student)
addStudentButton.grid(row=1,column=0,pady=25)

# Search Student Button
searchStudentButton=ttk.Button(leftFrame,text='Search Student',width=30,cursor='hand2',state=DISABLED,command=search_student)
searchStudentButton.grid(row=3,column=0,pady=25)

# Update Student Button
updateStudentButton=ttk.Button(leftFrame,text='Update Student',width=30,cursor='hand2',state=DISABLED,command=update_student)
updateStudentButton.grid(row=5,column=0,pady=25)

# Delete Student Button
deleteStudentButton=ttk.Button(leftFrame,text='Delete Student',width=30,cursor='hand2',state=DISABLED,command=delete_student)
deleteStudentButton.grid(row=7,column=0,pady=25)

# Show Student Button
showStudentButton=ttk.Button(leftFrame,text='Show Student',width=30,cursor='hand2',state=DISABLED,command=show_student)
showStudentButton.grid(row=9,column=0,pady=25)

# Export Data Button
exportDataButton=ttk.Button(leftFrame,text='Export Data',width=30,cursor='hand2',state=DISABLED,command=export_data)
exportDataButton.grid(row=11,column=0,pady=25)

# Exit Button
exitButton=ttk.Button(leftFrame,text='Exit',width=30,cursor='hand2',command=exit_app)
exitButton.grid(row=13,column=0,pady=25)

# Right Frame
rightFrame=Frame(root)
rightFrame.place(x=500,y=80,width=900,height=700)

# Preview and ScrollBar
scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

global studentTable
studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile','Email','Gender','Address','D.O.B'),
                          xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)
scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)
studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile',text='Mobile')
studentTable.heading('Email',text='Email')
studentTable.heading('Gender',text='Gender')
studentTable.heading('Address',text='Address')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.config(show='headings')

studentTable.column('Id', width=50, anchor=CENTER)
studentTable.column('Name', width=200, anchor=CENTER)
studentTable.column('Mobile', width=120, anchor=CENTER)
studentTable.column('Email', width=300, anchor=CENTER)
studentTable.column('Gender', width=80, anchor=CENTER)
studentTable.column('Address', width=300, anchor=CENTER)
studentTable.column('D.O.B', width=100, anchor=CENTER)

style=ttk.Style()
style.configure('Treeview',
                rowheight=30,
                font=('Arial', 12),
                background='#f4f4f4',
                foreground='#333333',
                fieldbackground='#f4f4f4')

style.configure('Treeview.Heading',
                font=('Arial', 13, 'bold'),
                foreground='white',
                background='#d3d3d3',
                relief='flat')

root.mainloop()