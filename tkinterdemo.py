from tkinter import *

root=Tk()
root.geometry("300x370")
root.title("My Tkinter Example")
root.resizable(widh=False,height=False)

l_id=Label(root,text="ID")
l_id.place(x=50,y=50)

l_fname=Label(root,text="FIRST NAME")
l_fname.place(x=50,y=100)

l_lname=Label(root,text="LAST NAME")
l_lname.place(x=50,y=150)

l_email=Label(root,text="EMAIL")
l_email.place(x=50,y=200)

l_mobile=Label(root,text="MOBILE")
l_mobile.place(x=50,y=250)

e_id=ENTRY(root)
e_id.place(x=150,y=50)

e_fname=ENTRY(root)
e_fname.place(x=150,y=100)

e_lname=ENTRY(root)
e_lname.place(x=150,y=150)

e_email=ENTRY(root)
e_email.place(x=150,y=200)

e_mobile=ENTRY(root)
e_mobile.place(x=150,y=250)

insert=Button(root,text="INSERT",bg="black",fg="white",font=("Arial",10))
insert.place(x=20,y=300)

search=Button(root,text="SEARCH",bg="black",fg="white",font=("Arial",10))
search.place(x=80,y=300)

update=Button(root,text="UPDATE",bg="black",fg="white",font=("Arial",10))
update.place(x=148,y=300)

delete=Button(root,text="DELETE",bg="black",fg="white",font=("Arial",10))
delete.place(x=214,y=300)

def create_conn():
    
















