# 📚 Student Management System

A feature-rich **Student Management System** built with **Python** and **MySQL**, offering a sleek and user-friendly interface developed using `Tkinter`. This system simplifies the management of student data with functionalities such as adding, searching, updating, deleting, and exporting records.

---

## 🔧 Features

### 🔐 **Login System**
- Secure login page to authenticate users.
- Validates against empty fields and incorrect credentials.

### 🏛️ **Student Management**
- **Add Student**: Add new student details such as name, age, gender, course, and email.
- **Search Student**: Locate students using filters like name, ID, or other attributes.
- **Update Student**: Modify existing student records with ease.
- **Delete Student**: Safely remove student data from the database.
- **Show Students**: Display all student records in a tabular format.

### 📈 **Export Data**
- Export student data to a **CSV** file, making it accessible in tools like Excel or Google Sheets.

### 🌍 **Database Integration**
- Fully integrated with **MySQL** for robust and secure data storage.
- Supports CRUD (Create, Read, Update, Delete) operations efficiently.

---

## 🛠️ Tech Stack

- **Frontend**: `Tkinter`
- **Backend**: `MySQL`
- **Programming Language**: Python

---

## 📘 How to Set Up and Use the System

### 1. Clone the Repository
Download the project from GitHub using the following command:
```bash
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system
```

### 2. Install MySQL and Create the Database
- Install **MySQL** on your system if not already installed.
- Create the database and table structure using the following SQL script:
```
CREATE TABLE IF NOT EXISTS student(
                    id INT NOT NULL PRIMARY KEY, 
                    name VARCHAR(50), 
                    mobile VARCHAR(30), 
                    email VARCHAR(50), 
                    gender VARCHAR(30), 
                    address VARCHAR(50), 
                    D_O_B VARCHAR(50))
```


### 3. Configure the Database Connection
Update the `config.py` file with your MySQL credentials:
```
LOGIN_USERNAME="ABC"
LOGIN_PASSWORD="1234"
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "your password"
MYSQL_DATABASE = "student_management"

```

### 5. Run the Application
Start the program by running the `login.py` file:
```bash
python login.py
```

### 6. Using the System
- **Login**: Use the default credentials (`username: admin, password: admin`) to log in.
- **Dashboard**: Navigate to the dashboard for all student management functionalities.
- **Export**: Export the displayed student data to a CSV file by clicking the "Export" button.

---

## 📅 Screenshots

### 🔐 Login Page
![Login Page](assets/screenshots/login.png)

### 🏛️ Home
![Home](https://github.com/sameeran4218/Student-Management-System/blob/main/Student%20Management%20System/assets/screenshots/home.png)

### 📄 CSV Export Example
Exported CSV files can be opened in Excel or other spreadsheet tools:
![CSV Export](assets/screenshots/data.png)



## 💡 Key Learnings
- **Database Management**: Implemented CRUD operations with MySQL.
- **GUI Development**: Designed a user-friendly interface using `Tkinter` and `ttkbootstrap`.
- **Error Handling**: Ensured smooth user experience by addressing edge cases.
- **Data Export**: Enabled seamless data export to CSV format for external use.


