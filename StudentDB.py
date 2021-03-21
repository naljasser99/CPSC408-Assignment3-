import csv, sqlite3

# Connection to database :-------------------------------------------------------
conn = sqlite3.connect(r"C:\sqlite\db\StudnetDB.db")
print ("Connection successfully to StudentDB");

cur = conn.cursor()

# Creating database table students : -------------------------------------------
cur.executescript("""
DROP TABLE IF EXISTS Students;
CREATE TABLE Students
             (StudentId INTEGER PRIMARY KEY AUTOINCREMENT,
             FirstName TEXT,
             LastName TEXT,
             GPA REAL,
             Major TEXT,
             FacultyAdvisor TEXT,
             Address TEXT,
             City TEXT,
             State TEXT,
             ZipCode TEXT,
             MobilePhoneNumber TEXT,
             isDeleted INTEGER);""")
print ("Students Table created successfully");
#-------------------------------------------------------------------------------

# Code to read csv file and import into students table :------------------------
def ReadCSV():
    with open("students.csv", "rt") as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        for row in csvReader:
            to_db = [row[0],
                     row[1],
                     row[2],
                     row[3],
                     row[4],
                     row[5],
                     row[6],
                     row[7],
                     row[8],
                     'None',
                     0]
            conn = sqlite3.connect(r"C:\sqlite\db\StudnetDB.db")
            cur = conn.cursor()
            cur.execute("""INSERT INTO Students
                        (FirstName,
                        LastName,
                        Address,
                        City,
                        State,
                        ZipCode,
                        MobilePhoneNumber,
                        Major,
                        GPA,
                        FacultyAdvisor,
                        isDeleted)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", to_db)
            conn.commit()
            conn.close()
    print ("CSV Imported");
#---------------------------------------------------------------------------------

# Code to Select all non deleted students from students table :-------------------
def SearchingAll():
    conn = sqlite3.connect(r"C:\sqlite\db\StudnetDB.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Students WHERE isDeleted = 0")
    rows = cur.fetchall()
    for row in rows:
        print(row);
#--------------------------------------------------------------------------------

# Code to Add student to students table : ---------------------------------------
def AddStudent():
    conn = sqlite3.connect(r"C:\sqlite\db\StudnetDB.db")
    cur = conn.cursor()
    print("Please insert required details : ");
    FirstName = input("Enter First Name of student : ")
    LastName = input("Enter Last Name of student : ")
    Address = input("Enter Address of student : ")
    City = input("Enter City of student : ")
    State = input("Enter State of student : ")
    ZipCode = input("Enter Zipcode of student : ")
    MobilePhoneNumber = input("Enter mobile number of student : ")
    Major = input("Enter major of student : ")
    GPA = input("Enter GPA of student : ")
    FacultyAdvisor = input("Enter faculty advosir of student : ")
    to_db = [FirstName,
             LastName,
             Address,
             City,
             State,
             ZipCode,
             MobilePhoneNumber,
             Major,
             GPA,
             FacultyAdvisor,
             0]
    cur.execute("""INSERT INTO Students
                        (FirstName,
                        LastName,
                        Address,
                        City,
                        State,
                        ZipCode,
                        MobilePhoneNumber,
                        Major,
                        GPA,
                        FacultyAdvisor,
                        isDeleted)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", to_db)
    conn.commit()
    conn.close()
    print("New student added successfully");
#---------------------------------------------------------------------------------

# Code for Update Student : ------------------------------------------------------
def UpdateStudent():
    conn = sqlite3.connect(r"C:\sqlite\db\StudnetDB.db")
    cur = conn.cursor()
    print("To Update student's Major, Advisor and MobileNumber insert Student ID :");
    StudentID = input("Enter Student ID of student : ")
    Choice = input("""Choose field you want to update :
                    A. Major
                    B. Advisor
                    C. MobilePhoneNumber
                    D. All above three
                    """)
    if Choice.lower() == ('a'):
        Major = input("Enter Major of student : ")
        Data = [Major, StudentID]
        cur.execute("UPDATE Students SET Major = ? WHERE StudentID = ?", Data)
        conn.commit()
        conn.close()
        print("Major update successfully for student id : ",StudentID)
    elif Choice.lower() == ('b'):
        Advisor = input("Enter Advisor of student : ")
        Data = [Advisor, StudentID]
        cur.execute("UPDATE Students SET FacultyAdvisor = ? WHERE StudentID = ?", Data)
        conn.commit()
        conn.close()
        print("Advisor update successfully for student id : ",StudentID)
    elif Choice.lower() == ('c'):
        Phone = input("Enter MobilePhoneNumber of student : ")
        Data = [Phone, StudentID]
        cur.execute("UPDATE Students SET MobilePhoneNumber = ? WHERE StudentID = ?", Data)
        conn.commit()
        conn.close()
        print("MobilePhoneNumber update successfully for student id : ",StudentID)
    elif Choice.lower() == ('d'):
        Major = input("Enter Major of student : ")
        Advisor = input("Enter Advisor of student : ")
        Phone = input("Enter MobilePhoneNumber of student : ")
        DataToUpdate = [Major, Advisor, Phone, StudentID]
        cur.execute("UPDATE Students SET Major = ?, Phone = ? ,MobilePhoneNumber = ? WHERE StudentID = ?", DataToUpdate)
        conn.commit()
        conn.close()
        print("Data update successfully for student id : ",StudentID)
#---------------------------------------------------------------------------------

# Code to Delete student :--------------------------------------------------------
def DeleteStudent():
    conn = sqlite3.connect(r"C:\sqlite\db\StudnetDB.db")
    cur = conn.cursor()
    print("To Delete student please insert Student ID :");
    StudentID = input("Enter Student ID of student : ")
    Data = [1, StudentID]
    cur.execute("UPDATE Students SET isDeleted = ? WHERE StudentID = ?", Data)
    conn.commit()
    conn.close()
    print("Student with student ID", StudentID, " deleted successfully");
#---------------------------------------------------------------------------------

# Code to search by GPA of student :----------------------------------------------
def SearchByGPA():
    conn = sqlite3.connect(r"C:\sqlite\db\StudnetDB.db")
    cur = conn.cursor()
    print("To Search student(s) with GPA please insert GPA :");
    GPA = input("Enter GPA of student(s) : ")
    cur.execute("SELECT * FROM Students WHERE GPA = ?", (GPA,))
    rows = cur.fetchall()
    for row in rows:
        print(row);
    conn.close()
#---------------------------------------------------------------------------------

# Code to search by City of student :---------------------------------------------
def SearchByCity():
    conn = sqlite3.connect(r"C:\sqlite\db\StudnetDB.db")
    cur = conn.cursor()
    print("To Search student(s) with City please insert City Name :");
    City = input("Enter City name of student(s) : ")
    cur.execute("SELECT * FROM Students WHERE City = ?", (City,))
    rows = cur.fetchall()
    for row in rows:
        print(row);
    conn.close()
#---------------------------------------------------------------------------------

# Code to search by State of student :--------------------------------------------
def SearchByState():
    conn = sqlite3.connect(r"C:\sqlite\db\StudnetDB.db")
    cur = conn.cursor()
    print("To Search student(s) with State please insert State Name :");
    State = input("Enter State name of student(s) : ")
    cur.execute("SELECT * FROM Students WHERE State = ?", (State,))
    rows = cur.fetchall()
    for row in rows:
        print(row);
    conn.close()
#---------------------------------------------------------------------------------

# Code to search by Advisor of student :------------------------------------------
def SearchByAdvisor():
    conn = sqlite3.connect(r"C:\sqlite\db\StudnetDB.db")
    cur = conn.cursor()
    print("To Search student(s) with Advisor please insert Advisor :");
    Advisor = input("Enter Advisor of student(s) : ")
    cur.execute("SELECT * FROM Students WHERE FacultyAdvisor = ?", (Advisor,))
    rows = cur.fetchall()
    for row in rows:
        print(row);
    conn.close()
#---------------------------------------------------------------------------------

    
    
# Calling function to read and import csv file in table students:-----------------
ReadCSV()
#---------------------------------------------------------------------------------

# Getting user choice to perform appropriate operations :-------------------------
while True:
    userChoice = input("""
        Choose options from A to I:
          A. Display all students
          B. Add new student
          C. Update student
          D. Delete student
          E. Search By GPA
          F. Search By City
          G. Search By State
          H. Search By Advisor
          I. Exit
        """)
    if userChoice.lower() not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'):
        print("Please select appropriate choice.")
    else:
        if userChoice.lower() == ('a'): #Display all non deleted students
            print("Displaying all Students :");
            SearchingAll()
            print("------------------------");
        elif userChoice.lower() == ('b'): #Add new student
            AddStudent()
            print("------------------------");
        elif userChoice.lower() == ('c'): # Update student
            UpdateStudent()
            print("------------------------");
        elif userChoice.lower() == ('d'): # Delete student
            DeleteStudent()
            print("------------------------");
        elif userChoice.lower() == ('e'): # Search By GPA
            SearchByGPA()
            print("------------------------");
        elif userChoice.lower() == ('f'): # Search By City
            SearchByCity()
            print("------------------------");
        elif userChoice.lower() == ('g'): # Search By State
            SearchByState()
            print("------------------------");
        elif userChoice.lower() == ('h'): # Search By Advisor
            SearchByAdvisor()
            print("------------------------");
        elif userChoice.lower() == ('i'): #exit
            break; # Terminate the user choice asking if user selected exit
        else:
            break  #default
