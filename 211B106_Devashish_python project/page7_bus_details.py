from tkinter import*
from tkinter.messagebox import*
import sqlite3

root=Tk()
root.title('Bus_Details')
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
fr=Frame(root)
fr.grid(row=0,column=2,columnspan=10)
img_Bus=PhotoImage(file=".\\Bus_for_project.png")
Label(fr,image=img_Bus).grid(row=0,column=2,padx=w//15)
fr.grid(row=1,column=2,columnspan=10)
Label(fr,text="Online Bus Booking System",font="Arial 30 bold",bg="light blue",fg="red").grid(row=1,column=2,pady=40) 
Label(root,text='Add Bus Details',font="Arial 20 bold",bg="white",fg="green" ).grid(row=2,column=2,columnspan=10)

con=sqlite3.Connection('bus_booking_database')
cur=con.cursor()
cur.execute('create table if not exists operator(operator_id number PRIMARY KEY,name varchar(20),address varchar(20),phone int(10),email varchar(20))')
cur.execute('create table if not exists bus(bus_id number PRIMARY KEY,type varchar(30),capacity int(5),fare number, operator_id number,route_id number,foreign key(operator_id) references operator(operator_id),foreign key(bus_id) references runs(bus_id),foreign key(route_id) references route(route_id))')
cur.execute('create table if not exists route(route_id number ,station_name varchar(20),station_id  number,PRIMARY KEY(route_id,station_id))')
cur.execute('create table if not exists runs(bus_id number,date date ,seat_aval number,PRIMARY KEY(bus_id,date))')
cur.execute('create table if not exists history(pasg_name varchar(20),Gender varchar(12),no_of_seats number,mobile_no number PRIMARY KEY,age number,bus_select number,too varchar(13),fr varchar(13),date date,fare number)')



Label(root,text='Bus Id',font="Arial 12 bold").grid(row=3,column=1)
bus_id=Entry(root,font="Arial 12 bold")        
bus_id.grid(row=3,column=2)

Label(root,text='Bus Type',font="Arial 12 bold").grid(row=3,column=3)
Bus_type=StringVar()
opt=["AC 2X2","AC 3X2","Non AC 3X2","Non AC 2X2","Non-AC-Sleeper 2X1","AC-Sleeper 2X1"]
Bus_type.set('Bustype')
d_menu=OptionMenu(root,Bus_type,*opt).grid(row=3,column=4)          

Label(root,text='Capacity',font="Arial 12 bold").grid(row=3,column=5)
bus_cap=Entry(root,font="Arial 12 bold")
bus_cap.grid(row=3,column=6,padx=0)

Label(root,text='Fare Rs',font="Arial 12 bold").grid(row=3,column=7,padx=0)
fare=Entry(root,font="Arial 12 bold")
fare.grid(row=3,column=8,padx=0)

Label(root,text='Operator ID',font="Arial 12 bold").grid(row=3,column=9,padx=0)
op_id=Entry(root,font="Arial 10 bold")
op_id.grid(row=3,column=10,padx=0)

Label(root,text='Route ID',font="Arial 12 bold").grid(row=3,column=11,padx=0)
route_id=Entry(root,font="Arial 12 bold")
route_id.grid(row=3,column=12,pady=90)

def bus_details1():
    if len(op_id.get())==0 or len(route_id.get())==0 or len(fare.get())==0 or len(bus_cap.get())==0 or len(bus_id.get())==0:
        showerror('Value Missing','Please Enter The Values')
    elif(op_id.get().isalpha()):
        showerror('Error','Enter Operator Id in numeric')
    elif(route_id.get().isalpha()):
        showerror('Error','Enter Route Id in numeric')
    elif(fare.get().isalpha()):
        showerror('Error','Enter Fare in numeric')
    elif(bus_cap.get().isalpha()):
        showerror('Error','Enter Capacity in numeric')
    elif(bus_id.get().isalpha()):
        showerror('Error','Enter Bus id in numeric')
    else:
        z=(bus_id.get(),Bus_type.get(),bus_cap.get(),fare.get(),op_id.get(),route_id.get())
        q=('insert into bus(bus_id,type,capacity,fare,route_id,operator_id) values(?,?,?,?,?,?)')
        cur.execute(q,z)
        con.commit()
        op_id.delete(0,END)
        route_id.delete(0,END)
        fare.delete(0,END)
        bus_cap.delete(0,END)
        bus_id.delete(0,END) 
        showinfo('Add Bus Entry','Bus Record Added')
        cur.execute('select * from bus')
        res=cur.fetchall()
        print(res)
    
        
def Edit_Bus():
    if len(op_id.get())==0 or len(route_id.get())==0 or len(fare.get())==0 or len(bus_cap.get())==0 or len(bus_id.get())==0:
        showerror('Value Missing','Please Enter The Values')
    elif(op_id.get().isalpha()):
        showerror('Error','Enter Operator Id in numeric')
    elif(route_id.get().isalpha()):
        showerror('Error','Enter Route Id in numeric')
    elif(fare.get().isalpha()):
        showerror('Error','Enter Fare in numeric')
    elif(bus_cap.get().isalpha()):
        showerror('Error','Enter Capacity in numeric')
    elif(bus_id.get().isalpha()):
        showerror('Error','Enter Bus id in numeric')
    else:
        z1=(bus_id.get())
        q1='select * from bus where bus_id=?'
        cur.execute(q1,z1)
        resss=cur.fetchall()
        if(resss):
            showinfo('Found','record found')
            x=(Bus_type.get(),bus_cap.get(),fare.get(),route_id.get(),op_id.get(),bus_id.get())
            q5='update bus set type=?,capacity=?,fare=?,route_id=?,operator_id =? where bus_id=?'
            cur.execute(q5,x)
            con.commit()
            cur.execute('select * from bus')
            result6=cur.fetchall()
            print(result6)
            showinfo('Bus Entry Edit','Bus Record Edited Successfully') 
        else:
            showerror('not found','error')
        op_id.delete(0,END)
        route_id.delete(0,END)
        fare.delete(0,END)
        bus_cap.delete(0,END)
        bus_id.delete(0,END)    
        print(resss)
        
 
Button(root,text="Add Bus",font="Arial 15 bold",bg="light green",command=bus_details1).grid(row=4,column=7)    
Button(root,text="Edit Bus",font="Arial 15 bold",bg="light green",command=Edit_Bus).grid(row=4,column=8)
Home_img=PhotoImage(file=".\\home.png")    
Button(root,image=Home_img,bg="green").grid(row=4,column=9)       

root.mainloop()
