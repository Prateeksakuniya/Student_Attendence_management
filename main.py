# Attendance Management System

# User database (in-memory, for demonstration purposes)
users_db = {"a":"a"}

# Student/Employee Database (in-memory, for demonstration purposes)
student_employee_db = {}

# Attendance Database (in-memory, for demonstration purposes)
attendance_db = {}

# TASK 1: USER LOG IN

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    stored_password = users_db.get(username)
    if stored_password == password:
        print(f"Login successful. Welcome, {username}!")
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False

# Task 2: Student Information Management
def add_student_employee(id, name):
    with open("student.txt" , "a") as file:
        student_employee_db[id] = name
        print("Student/employee added successfully.")
        file.write(f"{id}: {name}\n\n")

def view_student_employee():
    with open("student.txt" , "r") as file:
        id = input("Enter student/employee ID to view information: ")
        students=[]
        students = file.readlines()
        temp = []
        id_list = []
        name_list = []
        for line in students:
            temp.append(line.split(':')) 
        for i in temp:
            id_list.append(i[0])   
            temp = i[1].split('\n')
            name_list.append(temp[0])
            
        # print(id_list, name_list)
        index = -1
        for i in range(len(id_list)):
            if id_list[i] == id:
                index = i
                name = name_list[i]
                break
        if index != -1:
            print("\n\n\nVoila :)\nSTUDENT FOUND")
            print("ID: {}, Name: {}".format(id, name))
            print("\n\n")
        else:
            print('\n\nNot found in database!!\n\n')


def update_student_employee():
#     with open("student.txt", "w") as file:
#         id = input("Enter student/employee ID to update information: ")
#         if id in student_employee_db:
#             new_name = input("Enter the new name for student/employee: ")
#             student_employee_db[id] = new_name
#             print("Information updated successfully.")
#         else:
#             print("Student/employee with ID {} not found.".format(id))
#         file.write(f"{id}, {new_name}\n")
      with open("student.txt") as file:
        data=file.read()
        id=input("\nEnter id: ")
        
        if id in data:
            updated_value=input("\nEnter updated id: ")
            data=data.replace(id,updated_value)
        else:
            print("\n Given id does not exist....")
        with open("student.txt","w") as file:   
            file.write(data)        

def delete_student_employee():
    id = input("Enter student/employee ID to delete: ")
    found = False
    
    with open("student.txt", "r") as file:
        lines = file.readlines()
    new_lines = []
    for line in lines:
        if id not in line:
            new_lines.append(line)
        else:
            found = True
    with open("student.txt", "w") as file:
        file.writelines(new_lines)
    
    if found:
        print("Student/employee with ID {} deleted successfully.".format(id))
    else:
        print("Student/employee with ID {} not found.".format(id))

# Task 3: Marking Attendance
def mark_attendance():
    date = input("Enter the date (YYYY-MM-DD): ")
    print("Select an option:")
    print("1. Mark attendance for an individual")
    print("2. Mark attendance for a group")
    choice = input("Enter your choice: ")
    if choice == '1':
        student_employee_id = input("Enter student/employee ID: ")
        if student_employee_id in student_employee_db:
            attendance_db.setdefault(date, {})[student_employee_id] = True
            print("Attendance marked successfully.")
        else:
            print("Invalid student/employee ID.")
    elif choice == '2':
        group_size = int(input("Enter the number of students/employees in the group: "))
        for i in range(group_size):
            student_employee_id = input("Enter student/employee ID {}: ".format(i + 1))
            if student_employee_id in student_employee_db:
                attendance_db.setdefault(date, {})[student_employee_id] = True
                print("Attendance marked for student/employee ID {}: {}".format(student_employee_id, date))
            else:
                print("Invalid student/employee ID:", student_employee_id)


# Task 4: Viewing Attendance Records
def view_attendance_records():
    date = input("Enter the date (YYYY-MM-DD) to view attendance records: ")
    if date in attendance_db:
        print("Attendance records for {}:".format(date))
        for student_employee_id in attendance_db[date]:
            print("ID: {}, Name: {}".format(student_employee_id, student_employee_db.get(student_employee_id, "Unknown")))
    else:
        print("No attendance records found for {}.".format(date))

# Task 5: Generating Reports
def generate_monthly_report():
    # Implementation for generating monthly attendance report
    month_year = input("Enter the month and year (MM-YYYY) for the report: ")
    report_data = {}

    for date, attendance_records in attendance_db.items():
        if date.startswith(month_year):
            for student_employee_id, is_present in attendance_records.items():
                report_data.setdefault(student_employee_id, []).append(is_present)

    if report_data:
        print("Monthly Attendance Report for {}:".format(month_year))
        print("Student/Employee ID | Total Days | Present Days | Absent Days")
        for student_employee_id, attendance_list in report_data.items():
            total_days = len(attendance_list)
            present_days = sum(attendance_list)
            absent_days = total_days - present_days
            print("{:<18} | {:<10} | {:<12} | {:<11}".format(student_employee_id, total_days, present_days, absent_days))
    else:
        print("No attendance records found for {}.".format(month_year))

def generate_weekly_report():
    # Implementation for generating weekly attendance report
    week_start_date = input("Enter the start date of the week (YYYY-MM-DD) for the report: ")
    report_data = {}

    for i in range(7):
        current_date = (datetime.datetime.strptime(week_start_date, "%Y-%m-%d") + datetime.timedelta(days=i)).strftime("%Y-%m-%d")
        attendance_records = attendance_db.get(current_date, {})
        for student_employee_id, is_present in attendance_records.items():
            report_data.setdefault(student_employee_id, []).append(is_present)

    if report_data:
        print("Weekly Attendance Report for the week starting from {}:".format(week_start_date))
        print("Student/Employee ID | Total Days | Present Days | Absent Days")
        for student_employee_id, attendance_list in report_data.items():
            total_days = len(attendance_list)
            present_days = sum(attendance_list)
            absent_days = total_days - present_days
            print("{:<18} | {:<10} | {:<12} | {:<11}".format(student_employee_id, total_days, present_days, absent_days))
    else:
        print("No attendance records found for the week starting from {}.".format(week_start_date))

def generate_daily_report():
    # Implementation for generating daily attendance report
    date = input("Enter the date (YYYY-MM-DD) for the report: ")
    attendance_records = attendance_db.get(date, {})

    if attendance_records:
        print("Daily Attendance Report for {}:".format(date))
        print("Student/Employee ID | Attendance")
        for student_employee_id, is_present in attendance_records.items():
            attendance_status = "Present" if is_present else "Absent"
            print("{:<18} | {:<10}".format(student_employee_id, attendance_status))
    else:
        print("No attendance records found for {}.".format(date))

# Main Menu
def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Login")
        print("2. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
           option=login_user()
           if option==True:
            while True:
              print("1. Add Student/Employee")
              print("2. View Student/Employee")
              print("3. Update Student/Employee")
              print("4. Delete Student/Employee")
              print("5. Mark Attendance")
              print("6. View Attendance Records")
              print("7. Generate Monthly Report")
              print("8. Generate Weekly Report")
              print("9. Generate Daily Report")
              choice = input("Enter your choice: ")
              if choice == '1':
                  id = input("Enter student/employee ID: ")
                  name = input("Enter student/employee name: ")
                  add_student_employee(id, name)
              elif choice == '2':
                  view_student_employee()
              elif choice == '3':
                  update_student_employee()
              elif choice == '4':
                  delete_student_employee()
              elif choice == '5':
                  mark_attendance()
              elif choice == '6':
                  view_attendance_records()
              elif choice == '7':
                  generate_monthly_report()
              elif choice == '8':
                  generate_weekly_report()
              elif choice == '9':
                  generate_daily_report()
              else:
                  print("Invalid choice. Please try again.")
                  break
           else:
              print("check username and pass")
        elif choice==2:
          print("exit")
          break
        else:
          print("Enter valid choice")

if __name__ == "__main__":
    main_menu()

