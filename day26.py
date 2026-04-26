import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    
    database="broadwayclass"
)

cursor = db.cursor()


def create_student():
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    address = input("Enter Address: ")

    sql = "INSERT INTO studentinfo (FirstName, LastName, Address) VALUES (%s, %s, %s)"
    values = (first_name, last_name, address)

    cursor.execute(sql, values)
    db.commit()

    print("Student Added Successfully")


def read_students():
    cursor.execute("SELECT * FROM studentinfo")
    result = cursor.fetchall()

    print("\n--- Student Records ---")
    for row in result:
        print(row)


def update_student():
    student_id = int(input("Enter Student ID to Update: "))
    new_first_name = input("Enter New First Name: ")
    new_last_name = input("Enter New Last Name: ")
    new_address = input("Enter New Address: ")

    sql = """
    UPDATE studentinfo
    SET FirstName=%s, LastName=%s, Address=%s
    WHERE id=%s
    """

    values = (new_first_name, new_last_name, new_address, student_id)

    cursor.execute(sql, values)
    db.commit()

    print("Student Updated Successfully")


def delete_student():
    student_id = int(input("Enter Student ID to Delete: "))

    sql = "DELETE FROM studentinfo WHERE id=%s"
    values = (student_id,)

    cursor.execute(sql, values)
    db.commit()

    print("Student Deleted Successfully")


while True:
    print("\n===== STUDENT CRUD SYSTEM =====")
    print("1. Insert Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        create_student()

    elif choice == "2":
        read_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")