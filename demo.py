
import psycopg2

def create_table():
     conn = psycopg2.connect(dbname="studentdb",user ="postgres",password="admin123", host="localhost",port="5432")
     cur =conn.cursor()
     cur.execute("create table student(student_id serial primary key,name text, address text,age int,number text);")
     print("Student table created")
     conn.commit()
     conn.close()

def insert_data():
     name = input("Enter Name: ")
     address = input("Enter Address: ")
     age = input("Enter Age: ")
     number = input("Enter Number: ")
     conn = psycopg2.connect(dbname="studentdb", user="postgres", password="admin123", host="localhost", port="5432")
     cur = conn.cursor()
     cur.execute("insert into  student(name,address,age,number) values(%s,%s,%s,%s)",(name,address,age,number))
     print("data added to Student table ")
     conn.commit()
     conn.close()

def read_data():
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="admin123", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("select * from student;")
    student = cur.fetchall()
    for student in student:
        print(f"ID:{student[0]},name:{student[1]},address:{student[2]},age:{student[3]},number:{student[4]}")
    conn.commit()
    conn.close()
def delete_data():
    student_id = input("Enter id of the student to be delete: ")
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="admin123", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("select * from student where student_id=%s",(student_id,))
    student =cur.fetchone()

    if student:
        print(f"student to be deleted: ID {student[0]}, name:{student[1]},address:{student[2]},age:{student[3]},number:{student[4]}")
        choice =input("Are you sure want to delete  the student ? (yes/no): ")
        if choice.lower()=="yes":
            cur.execute("delete from student where student_id=%s",(student_id))
            print("student record  deleted ")
        else: print("deletion cancelled ")
    else: print("student not found ")
    conn.commit()
    conn.close()

def update_data():
    student_id = input("Enter id of the student to be updated: ")
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="admin123", host="localhost", port="5432")
    cur = conn.cursor()
    fields ={
         "1":("name","Enter the new name: "),
         "2":("address","Enter the new Address: "),
         "3":("age","Enter the new age: "),
         "4":("number","Enter the new number: ")
    }
    print("which field would you  like to update ")
    for key in fields:
        print(f"{key}:{fields[key][0]}")

    field_choice = input("enter the number of the field you want to update: ")
    if field_choice in fields:
        field_name, promt =fields[field_choice]
        print(field_name, promt)
        new_value =input(promt)
        sql=f"update student set {field_name}=%s where student_id=%s"
        cur.execute(sql,(new_value,student_id))
        print(f"{field_name} updated successfully")
    else:
        print("Invalid choice ")

    conn.commit()
    conn.close()


while True:
    print("\n welcome to student database management system ")
    print("1. Create Table")
    print("2. Insert Data")
    print("3. Read Data")
    print("4. Update Data")
    print("5. Delete Data")
    print("6. Exit")
    choice =input("\n Enter Your choice (1-6): ")
    if choice== '1':
        create_table()
    elif choice == '2': insert_data()
    elif choice == '3': read_data()
    elif choice == '4': update_data()
    elif choice == '5': delete_data()
    elif choice == '6':
        print("Exiting the program.")
        break

    else: print("Invalid Choice, please enter a number between 1-6: ")

