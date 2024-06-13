
import sqlite3
con=sqlite3.Connection('bus_booking_database')
cur=con.cursor()
   
from tkinter import*
from tkinter.messagebox import *

root=Tk()

root.title('Operator Details')
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
fr=Frame(root)

cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,name varchar(20),address varchar(20),phone int(10),email varchar(20))')
cur.execute('create table if not exists bus(bus_id number PRIMARY KEY,type varchar(30),capacity int(5),fare number, operator_id number,route_id number,foreign key(operator_id) references operator(operator_id),foreign key(bus_id) references runs(bus_id),foreign key(route_id) references route(route_id))')
cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
cur.execute('create table if not exists runs(bus_id number,date date ,seat_aval number,PRIMARY KEY(bus_id,date))')
cur.execute('create table if not exists history(pasg_name varchar(20),Gender varchar(12),no_of_seats number,mobile_no number PRIMARY KEY,age number,bus_select number,too varchar(13),fr varchar(13),date date,fare number)')


fr.grid(row=0,column=0,columnspan=100)
img_Bus=PhotoImage(file=".\\Bus_for_project.png")
Label(fr,image=img_Bus).grid(row=0,column=0,padx=w//10+420,columnspan=100)
fr.grid(row=1,column=0,columnspan=100)

operator_id=0
operator_name=0
phone_no=0
dddress=0    
mail=0

Label(fr,text="Online Bus Booking System",font="Arial 30 bold",bg="light blue",fg="red").grid(row=1,column=0,pady=40,columnspan=100) 
Label(root,text='Add Bus Operator Details',font="Arial 17 bold",bg="white",fg="green" ).grid(row=2,column=0,columnspan=100,pady=5) 

Label(root,text='Operator id',font="Arial 11 bold").grid(row=3,column=47)
operator_id=Entry(root,font="Arial 10 bold")     
operator_id.grid(row=3,column=48)

Label(root,text='Name',font="Arial 11 bold").grid(row=3,column=49)
operator_name=Entry(root,font="Arial 10 bold")
operator_name.grid(row=3,column=50)          

Label(root,text='Address',font="Arial 11 bold").grid(row=3,column=51)
address=Entry(root,font="Arial 10 bold")
address.grid(row=3,column=52)

Label(root,text='Phone',font="Arial 11 bold").grid(row=3,column=53)
ph_no=Entry(root,font="Arial 10 bold")     
ph_no.grid(row=3,column=54)

Label(root,text='Email',font="Arial 11 bold").grid(row=3,column=55)
mail=Entry(root,font="Arial 10 bold")     
mail.grid(row=3,column=56)

def details():
    if(len(operator_id.get())==0 or len(operator_name.get())==0 or len(address.get())==0 or len(ph_no.get())==0 or len(mail.get())==0):
        showerror('Value Missing','Please Enter The Values')
    elif(operator_id.get().isalpha()):
        showerror('Error','Enter Operator Id in numeric')
    elif(operator_name.get().isnumeric()):
        showerror('Error','Enter Operator Name correctly')
    elif(address.get().isnumeric()):
        showerror('Error','Enter Address correctly')
    elif(ph_no.get().isalpha()):
        showerror('Error','Enter Mobile no. correctly')
    elif(len(ph_no.get())!=10):
        showerror('Error','Enter Mobile no. correctly 10 digits')
    else:
        operatorid1=operator_id.get()
        operatorname1=operator_name.get()
        address_op1=address.get()
        phoneno1=ph_no.get()
        operatoremail1=mail.get()

        q='insert into operator(operator_id,Name,address,phone,email) values(?,?,?,?,?)'
        v=(operatorid1,operatorname1,address_op1,phoneno1,operatoremail1)
        cur.execute(q,v)
        con.commit()
        cur.execute('select * from operator')
        res=cur.fetchall()
        Label(root,text=res,font='arial 11 bold').grid(row=4,column=10,columnspan=100)
        
        operator_id.delete(0,END)
        operator_name.delete(0,END)
        address.delete(0,END)
        ph_no.delete(0,END)
        mail.delete(0,END)
        showinfo('Operator Entry','Operator Record Added successfully')
        print(res)
        
def edit_details():
    if(len(operator_id.get())==0 or len(operator_name.get())==0 or len(address.get())==0 or len(ph_no.get())==0 or len(mail.get())==0):
        showerror('Value Missing','Please Enter The Values')
    elif(operator_id.get().isalpha()):
        showerror('Error','Enter Operator Id in numeric')
    elif(operator_name.get().isnumeric()):
        showerror('Error','Enter Operator Name correctly')
    elif(address.get().isnumeric()):
        showerror('Error','Enter Address correctly')
    elif(ph_no.get().isalpha()):
        showerror('Error','Enter Mobile no. correctly')
    elif(len(ph_no.get())!=10):
        showerror('Error','Enter Mobile no. correctly 10 digits')
    else:
        operatorid1=operator_id.get()
        operatorname1=operator_name.get()
        address_op1=address.get()
        phoneno1=ph_no.get()
        operatoremail1=mail.get()
        del_id=operator_id.get()
        q1=('select operator_id from operator where operator_id=?')
        cur.execute(q1,operatorid1)
        result4=cur.fetchall()
        if(result4):
            showinfo('Found','Operator ID Exist')
            qu1='update operator set name=?,address=?,phone=?,email=? where operator_id=?'
            va1=(operatorname1,address_op1,phoneno1,operatoremail1,operatorid1)
            cur.execute(qu1,va1)
            con.commit()

            qu2='select * from operator where operator_id=?'
            cur.execute(qu2,operatorid1)
            result5=cur.fetchall()            
            Label(root,text=result5,font='arial 11 bold').grid(row=4,column=10,columnspan=100)
            
            operator_id.delete(0,END)
            operator_name.delete(0,END)
            address.delete(0,END)
            ph_no.delete(0,END)
            mail.delete(0,END)
            showinfo('Operator Entry','Operator Record updated')
        else:
            showerror('not found!','operator id does not exists!!!')
                
Button(root,text="Add",font="Arial 15 bold",bg="light green",command=details).grid(row=3,column=58,padx=0)   
Button(root,text="Edit",font="Arial 15 bold",bg="light green",command=edit_details).grid(row=3,column=60,pady=20)
img1=PhotoImage(file=".\\home.png")    
Button(root,image=img1,bg="light green").grid(row=3,column=61)



root.mainloop()
