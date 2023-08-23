# def update_student_employee():
#     with open("student.txt") as file:
#         data=file.read()
#         print(data)
#         if "1234" in data:
#             data=data.replace("1234","prateek")
#     with open("student.txt","w") as f2:   
#         f2.write(data)
                    
# # update_student_employee()

# # def view_student_employee():
# #     with open("student.txt" , "r") as file:
# #         id = input("Enter student/employee ID to view information: ")
# #         list1 = file.readline().split(sep=":")
# #         # print(type(list1[0]))
# #         if id == list1[0]:
# #             print("ID: {}, Name: {}".format(id, list1[1]))
# #         else:
# #             print("Student/employee with ID {} not found.".format(id))
# #         # students=file.read()
# #         # print(students)
# # view_student_employee()

# def view_student_employee():
#     id_to_find = input("Enter student/employee ID to view information: ")
    
#     with open("student.txt", "r") as file:
#         found = False  # Flag to check if the ID is found
        
#         for line in file:
#             id_, name = line.split(":")
#             if id_ == id_to_find:
#                 print("ID: {}, Name: {}".format(id_, name))
#                 found = True
#                 break
        
#         if not found:
#             print("Student/employee with ID {} not found.".format(id_to_find))

# view_student_employee()
with open("try.txt","w") as file:
    id=input("Enter id: ")
    name=input("Enter name:")
    city=input("Enter city")
    # data={"Id":id,"Name":name}
    data={"stud1":{"ID":id,"Name":name,"City":city}}
    file.write(str(data))
with open("try.txt") as file: 
    data=eval(file.read())
    print(data["stud1"]["ID"])
    print(data["stud1"]["Name"])
# data={"stud1":{"ID":id,"Name":name,"City":city}}
