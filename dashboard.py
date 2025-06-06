from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from course import CourseTab
from student import StudentTab
from result import ResultTab
from report import ReportTab
from database import Database
import os

db=Database()
con,cur=db.get_conenction()
class ManagementSystem:

    def __init__(self, root):
        self.root = root
        self.root.title('Student Management System')
        self.root.geometry('1300x700+120+50')
        self.root.config(bg='white')
        self.logo_dash=ImageTk.PhotoImage(file='assets/logo_p.png')
        # title
        title=Label(self.root,text='Student Management System',padx=15,compound=LEFT,image=self.logo_dash,font=('goudy old style',20,'bold'),bg='#033054',fg='white').place(x=0,y=0,relwidth=1,height=50)
        # Menu
        menuFrame=LabelFrame(self.root,text='Menus',font=('times new roman',15,),bg='white')
        menuFrame.place(x=70,y=70,width=1150,height=75)
        courseButton = Button(menuFrame, text='Course', font=('goudy old style', 15, 'bold'),
                              bg='#0b5377', fg='white', command=self.add_course, cursor='hand2')
        courseButton.place(x=10, y=1, width=150, height=40)

        studentButton = Button(menuFrame, text='Student', font=('goudy old style', 15, 'bold'),
                               bg='#0b5377', fg='white', command=self.add_student, cursor='hand2')
        studentButton.place(x=180, y=1, width=150, height=40)

        resultButton = Button(menuFrame, text='Result', font=('goudy old style', 15, 'bold'),
                              bg='#0b5377', fg='white', command=self.add_result, cursor='hand2')
        resultButton.place(x=350, y=1, width=150, height=40)

        viewButton = Button(menuFrame, text='View', font=('goudy old style', 15, 'bold'),
                            bg='#0b5377', fg='white', command=self.view_report, cursor='hand2')
        viewButton.place(x=520, y=1, width=150, height=40)

        logoutButton = Button(menuFrame, text='Logout', font=('goudy old style', 15, 'bold'),
                              bg='#0b5377', fg='white', command=self.logout, cursor='hand2')
        logoutButton.place(x=690, y=1, width=150, height=40)

        exitButton = Button(menuFrame, text='Exit', font=('goudy old style', 15, 'bold'),
                            bg='#0b5377', fg='white', command=self.exit, cursor='hand2')
        exitButton.place(x=860, y=1, width=150, height=40)

        refreshButton = Button(menuFrame, text='Refresh', font=('goudy old style', 15, 'bold'),
                               bg='#0b5377', fg='white', command=self.update_details, cursor='hand2')
        refreshButton.place(x=1030, y=1, width=100, height=40)
        # Content
        self.bgImage=Image.open('assets/bg.png')
        self.bgImage = self.bgImage.resize((920, 350), Image.Resampling.LANCZOS)
        self.bgImage=ImageTk.PhotoImage(self.bgImage)
        self.labelBg=Label(self.root,image=self.bgImage).place(x=200,y=200,width=920,height=350)
        # Details
        self.courseLabel = Label(self.root, text='Total Courses\n[0]', font=('goudy old style', 20),
                                 bd=10, relief=RIDGE, bg='#e43b06', fg='white')
        self.courseLabel.place(x=300, y=560, width=230, height=75)

        self.studentLabel = Label(self.root, text='Total Students\n[0]', font=('goudy old style', 20),
                                  bd=10, relief=RIDGE, bg='#0676ad', fg='white')
        self.studentLabel.place(x=550, y=560, width=230, height=75)

        self.resultLabel = Label(self.root, text='Total Results\n[0]', font=('goudy old style', 20),
                                 bd=10, relief=RIDGE, bg='#038074', fg='white')
        self.resultLabel.place(x=800, y=560, width=230, height=75)

        # Footer
        footer=Label(self.root,text='Student Management System\n Built for Efficient Management',font=('goudy old style',12,'bold'),
                     bg='#262626',fg='white').pack(side=BOTTOM,fill=X)

    def add_course(self):
        self.courseWin=Toplevel(self.root)
        self.courseObj=CourseTab(self.courseWin)

    def add_student(self):
        self.studentWin=Toplevel(self.root)
        self.studentObj=StudentTab(self.studentWin)

    def add_result(self):
        self.resWin=Toplevel(self.root)
        self.resObj=ResultTab(self.resWin)

    def view_report(self):
        self.rpWin=Toplevel(self.root)
        self.rpObj=ReportTab(self.rpWin)

    def logout(self):
        op=messagebox.askyesno('Confirm','Do you really want to logout?',parent=self.root)
        if op:
            self.root.destroy()
            os.system('python login.py')

    def exit(self):
        op=messagebox.askyesno('Confirm','Do you really eant to exit?',parent=self.root)
        if op:
            self.root.destroy()

    def update_details(self):
        try:
            cur.execute('SELECT COUNT(*) FROM courses')
            count = cur.fetchone()[0]
            self.courseLabel.config(text=f'Total Courses\n[{count}]')

            cur.execute('SELECT COUNT(*) FROM students')
            count = cur.fetchone()[0]
            self.studentLabel.config(text=f'Total Students\n[{count}]')

            cur.execute('SELECT COUNT(*) FROM results')
            count = cur.fetchone()[0]
            self.resultLabel.config(text=f'Total Results\n[{count}]')
        except Exception as e:
            messagebox.showerror('Error',f'{str(e)}')


if __name__ == '__main__':
    root = Tk()
    ms = ManagementSystem(root)
    root.mainloop()
