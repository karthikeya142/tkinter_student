from tkinter import *
from tkinter import ttk, messagebox

import psycopg2


def run_query(query,parameters=()):
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="admin123", host="localhost", port="5432")
    cur = conn.cursor()
    query_result= None
    try:
        cur.execute(query,parameters)
        if query.lower().startswith("select"):
            query_result =cur.fetchall()
        conn.commit()
    except psycopg2.Error as e:
        messagebox.showerror("Database Error",str(e))
    finally:
        cur.close()
        conn.close()
    return  query_result


def refresh_treeview():
    for item in tree.get_children():
        tree.delete(item)
    records = run_query("select * from student;")
    for record in records:
        tree.insert('',END,values=record)


def insert_data():
    query = "insert into students(name,address,age,numbrer) values(%s,%s,%s,%s)"
    parameters=(name_entry.get(),address_entry.get(),age_entry.get(),Phone_entry.get())
    run_query(query,parameters)
    messagebox.showinfo("Information","Data added sudccessfully")
    refresh_treeview()


root = Tk()
root.title("Student Management System")
frame = LabelFrame(root,text="Student data")
frame.grid(row=0,column=0,padx=10,pady=10,sticky='ew')

Label(frame, text="Name:").grid(row=0,column=0,padx=2,sticky="ew")
name_entry=Entry(frame).grid(row=0,column=1,pady=2,sticky="ew")

Label(frame, text="Address:").grid(row=1,column=0,padx=2,sticky="ew")
address_entry=Entry(frame).grid(row=1,column=1,pady=2,sticky="ew")

Label(frame, text="Age:").grid(row=2,column=0,padx=2,sticky="ew")
age_entry=Entry(frame).grid(row=2,column=1,pady=2,sticky="ew")

Label(frame, text="Phone Number:").grid(row=3,column=0,padx=2,sticky="ew")
Phone_entry=Entry(frame).grid(row=3,column=1,pady=2,sticky="ew")

button_frame=Frame(root).grid(row=0,column=0,pady=5,sticky="ew")
Button(button_frame,text="Create Table").grid(row=4,column=1,padx=5)
Button(button_frame,text="Add Data",command=insert_data).grid(row=4,column=2,padx=5)
Button(button_frame,text="Update Data").grid(row=4,column=3,padx=5)
Button(button_frame,text="Delete Data").grid(row=4,column=4,padx=5)

tree_frame=Frame(root)
tree_frame.grid(row=5,column=0, padx=10,sticky="nsew")

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)

tree=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,selectmode="browse")
tree.pack()
tree_scroll.config(command=tree.yview)
tree['columns']=("student_id","Name","Address","Age","Number")
tree.column("#0",width=0,stretch=NO)
tree.column("student_id",anchor=CENTER,width=80)
tree.column("Name",anchor=CENTER,width=120)
tree.column("Address",anchor=CENTER,width=120)
tree.column("Age",anchor=CENTER,width=50)
tree.column("Number",anchor=CENTER,width=120)

tree.heading("student_id",text="ID",anchor=CENTER)
tree.heading("Name",text="Name",anchor=CENTER)
tree.heading("Address",text="Address",anchor=CENTER)
tree.heading("Age",text="Age",anchor=CENTER)
tree.heading("Number",text="Phone Number",anchor=CENTER)




refresh_treeview()

root.mainloop()






